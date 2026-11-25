import json
from pathlib import Path
import tempfile
import unittest

from scripts.verify_collection import verify


class VerifyCollectionTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.member = self.root / "skills" / "sample"
        (self.member / "references").mkdir(parents=True)
        (self.member / "references" / "detail.md").write_text("# Evidence\n")
        (self.member / "LICENSE").write_text("fixture license")
        self.skill = self.member / "SKILL.md"
        self.skill.write_text(
            "---\nname: sample\ndescription: Evidence fixture\n---\n"
            "[Detail](references/detail.md)\n"
        )
        self.manifest = {
            "schema": 1, "name": "pennix-system-devel-skills",
            "skills": {"sample": {"path": "skills/sample", "license": "LICENSE"}},
            "commands": {}, "materialized": {},
        }
        self.save_manifest()

    def save_manifest(self):
        (self.root / "collection.json").write_text(json.dumps(self.manifest))

    def test_valid_member(self):
        self.assertEqual(verify(self.root), 1)

    def test_missing_member_license_cannot_use_root_license(self):
        (self.member / "LICENSE").rename(self.root / "LICENSE")
        with self.assertRaisesRegex(ValueError, "member license"):
            verify(self.root)

    def test_member_link_cannot_use_another_member_or_root(self):
        (self.root / "outside.md").write_text("# Outside\n")
        with self.skill.open("a") as out:
            out.write("[Outside](../../outside.md)\n")
        with self.assertRaisesRegex(ValueError, "out-of-member"):
            verify(self.root)

    def test_reference_link_checks_the_target_not_its_optional_title(self):
        with self.skill.open("a") as out:
            out.write('\n[Details][detail]\n\n[detail]: <references/detail.md> "Read this"\n')
        self.assertEqual(verify(self.root), 1)
        (self.member / "references" / "detail.md").unlink()
        self.skill.write_text(self.skill.read_text().replace(
            "[Detail](references/detail.md)\n", ""
        ))
        with self.assertRaisesRegex(ValueError, "out-of-member"):
            verify(self.root)

    def test_duplicate_yaml_is_rejected(self):
        self.skill.write_text("---\nname: wrong\nname: sample\ndescription: Duplicate\n---\n")
        with self.assertRaisesRegex(ValueError, "duplicate key: name"):
            verify(self.root)

    def test_description_length_counts_the_decoded_value(self):
        for description, valid in (("证" * 1024, True), (" " + "证" * 1024, False), (" ", False)):
            with self.subTest(length=len(description), valid=valid):
                value = json.dumps(description, ensure_ascii=False)
                self.skill.write_text(f"---\nname: sample\ndescription: {value}\n---\nEvidence\n")
                if valid:
                    self.assertEqual(verify(self.root), 1)
                else:
                    with self.assertRaisesRegex(ValueError, "invalid frontmatter"):
                        verify(self.root)

    def test_member_can_never_register_a_command(self):
        self.manifest["commands"] = {"sample": "sample/bin/main"}
        self.save_manifest()
        with self.assertRaisesRegex(ValueError, "command/materialization"):
            verify(self.root)

    def test_first_release_does_not_ship_unreviewed_member_files(self):
        for name in ("references/unlisted.py", "references/hidden/SKILL.md", "scripts/helper"):
            with self.subTest(name=name):
                path = self.member / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("not part of the documentation payload")
                with self.assertRaisesRegex(ValueError, "unexpected member file"):
                    verify(self.root)
                path.unlink()

    def test_license_must_be_separate_from_instructions(self):
        self.manifest["skills"]["sample"]["license"] = "SKILL.md"
        self.save_manifest()
        with self.assertRaisesRegex(ValueError, "member license"):
            verify(self.root)

    def test_metadata_alone_does_not_make_a_skill(self):
        self.skill.write_text("---\nname: sample\ndescription: No instructions\n---\n")
        with self.assertRaisesRegex(ValueError, "empty instructions"):
            verify(self.root)
