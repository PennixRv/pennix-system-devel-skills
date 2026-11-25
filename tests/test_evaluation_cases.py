import collections
import json
from pathlib import Path
import tempfile
import unittest

from evaluations.case import load_cases, render_prompt

ROOT = Path(__file__).resolve().parents[1]


class EvaluationCasesTests(unittest.TestCase):
    def test_manifest_members_have_independent_positive_and_control_cases(self):
        manifest = json.loads((ROOT / "collection.json").read_text())
        cases = load_cases(ROOT)
        coverage = collections.Counter((case["covers"], case["kind"]) for case in cases.values())
        self.assertEqual({name for name, kind in coverage}, set(manifest["skills"]))
        for member in manifest["skills"]:
            self.assertEqual(coverage[member, "positive"], 1)
            self.assertEqual(coverage[member, "control"], 1)
        for case_id in ("mixed-yocto-kconfig", "mixed-zephyr-gdb"):
            self.assertEqual(cases[case_id]["kind"], "mixed")

    def test_non_object_case_is_reported_as_invalid(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "evaluations").mkdir()
            (root / "evaluations/cases.json").write_text("[null]")
            with self.assertRaisesRegex(ValueError, "invalid evaluation case"):
                load_cases(root)

    def test_model_prompt_does_not_include_rubric_fields(self):
        case = load_cases(ROOT)["bitbake-image"]
        prompt = render_prompt(case)
        self.assertIn(case["request"], prompt)
        self.assertIn(case["given"], prompt)
        for field in ("id", "covers", "expect", "forbid"):
            self.assertNotIn(case[field], prompt)
