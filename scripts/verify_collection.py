#!/usr/bin/env python3
"""Check the source collection and the files that can follow each member."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
HEADER = re.compile(r"\A---\n(.*?)\n---(?:\n|$)", re.S)
LINK = re.compile(r"\]\(([^)\n]+)\)")
REFERENCE = re.compile(r"^ {0,3}\[[^\]]+\]:[ \t]*(<[^>]+>|\S+)")


def unique(pairs):
    mapping = {}
    for key, value in pairs:
        if key in mapping:
            raise ValueError(f"duplicate key: {key}")
        mapping[key] = value
    return mapping


class UniqueYaml(yaml.SafeLoader):
    pass


UniqueYaml.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    lambda loader, node: unique(loader.construct_pairs(node)),
)


def check_links(source, member):
    fence = None
    for line in source.read_text(encoding="utf-8").splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if marker and not fence:
            fence = marker[1]
            continue
        if marker and fence and marker[1].startswith(fence) and not marker[2].strip():
            fence = None
            continue
        if fence:
            continue
        # shortcut: check file targets in the collection's Markdown conventions, not arbitrary HTML or anchors.
        reference = REFERENCE.match(line)
        targets = [reference[1]] if reference else LINK.findall(re.sub(r"`+[^`]+`+", "", line))
        for raw in targets:
            link = raw.strip().strip("<>")
            target = urlsplit(link)
            if target.scheme == "https" and target.netloc:
                continue
            path = unquote(target.path)
            if target.scheme or target.netloc or path.startswith("/"):
                raise ValueError(f"{source}: unsupported link target {link}")
            if path:
                resolved = (source.parent / path).resolve()
                if not resolved.is_relative_to(member) or not resolved.is_file():
                    raise ValueError(f"{source}: missing or out-of-member link {link}")


def verify(root):
    manifest = json.loads((root / "collection.json").read_text(encoding="utf-8"),
                          object_pairs_hook=unique)
    if (not isinstance(manifest, dict)
            or set(manifest) != {"schema", "name", "skills", "commands", "materialized"}
            or type(manifest["schema"]) is not int or manifest["schema"] != 1
            or manifest["name"] != "pennix-system-devel-skills"
            or manifest["commands"] != {} or manifest["materialized"] != {}
            or not isinstance(manifest["skills"], dict) or not manifest["skills"]):
        raise ValueError("invalid collection header or nonempty command/materialization sections")
    if any(path.is_symlink() or not (path.is_dir() or path.is_file())
           for path in (root / "skills", *(root / "skills").rglob("*"))):
        raise ValueError("member tree contains a link or a special file")
    if set(manifest["skills"]) != {path.name for path in (root / "skills").iterdir()}:
        raise ValueError("collection manifest and member directories differ")

    for name, entry in manifest["skills"].items():
        if (not NAME.fullmatch(name) or len(name) > 64 or not isinstance(entry, dict)
                or set(entry) != {"path", "license"} or entry["path"] != f"skills/{name}"):
            raise ValueError(f"{name}: invalid member identity")
        member = root / entry["path"]
        license_path = entry["license"]
        if (license_path != "LICENSE"
                or not (member / license_path).is_file()
                or not (member / license_path).read_bytes().strip()):
            raise ValueError(f"{name}: missing or invalid member license")
        text = (member / "SKILL.md").read_text(encoding="utf-8")
        header = HEADER.match(text)
        metadata = yaml.load(header[1], Loader=UniqueYaml) if header else None
        if (not isinstance(metadata, dict) or metadata.get("name") != name
                or not isinstance(metadata.get("description"), str)
                or not 0 < len(metadata["description"].strip()) <= 1024):
            raise ValueError(f"{name}: invalid frontmatter")
        if not text[header.end():].strip():
            raise ValueError(f"{name}: empty instructions")
        for source in member.rglob("*"):
            if not source.is_file():
                continue
            path = source.relative_to(member)
            reference = (path.parts[0] == "references" and path.suffix == ".md"
                         and path.name != "SKILL.md"
                         and not any(part.startswith(".") for part in path.parts))
            if source.stat().st_mode & 0o111 or (
                    not reference and path.as_posix() not in {"SKILL.md", "LICENSE", "NOTICE", "NOTICE.md"}):
                raise ValueError(f"{name}: unexpected member file {path}")
            if path.suffix == ".md":
                check_links(source, member)
    return len(manifest["skills"])


if __name__ == "__main__":
    try:
        count = verify(Path(__file__).resolve().parents[1])
    except (ValueError, OSError, TypeError, yaml.YAMLError) as error:
        print(f"collection invalid: {error}", file=sys.stderr)
        sys.exit(1)
    print(f"verified {count} collection members")
