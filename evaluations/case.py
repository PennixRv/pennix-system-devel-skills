#!/usr/bin/env python3
"""Render a synthetic case without exposing the rubric to the evaluated model."""

import argparse
import json
from pathlib import Path


def load_cases(root):
    entries = json.loads((root / "evaluations/cases.json").read_text(encoding="utf-8"))
    cases = {}
    fields = {"id", "covers", "kind", "request", "given", "expect", "forbid"}
    for entry in entries:
        if (set(entry) != fields or any(not isinstance(v, str) or not v.strip() for v in entry.values())
                or entry["id"] in cases
                or entry["kind"] not in {"positive", "control", "mixed", "transfer"}):
            raise ValueError(f"invalid evaluation case: {entry}")
        cases[entry["id"]] = entry
    return cases


def render_prompt(case):
    return (
        "以下是合成工程场景。只分析所给材料，不访问网络、真实用户目录或真实目标，"
        "不执行构建、调试、部署或任何改变状态的命令。可按正常方式发现与阅读本会话可用的 Skill。\n\n"
        f"{case['request']}\n\n现有证据：\n{case['given']}"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case_id", nargs="?")
    parser.add_argument("--rubric", action="store_true", help="render private scoring criteria, not a prompt")
    args = parser.parse_args()
    cases = load_cases(Path(__file__).resolve().parents[1])
    if args.case_id is None and not args.rubric:
        print("\n".join(cases))
    elif args.case_id not in cases:
        parser.error("unknown case ID")
    elif args.rubric:
        case = cases[args.case_id]
        print(f"{case['covers']} / {case['kind']}\n预期：{case['expect']}\n禁止：{case['forbid']}")
    else:
        print(render_prompt(cases[args.case_id]))


if __name__ == "__main__":
    main()
