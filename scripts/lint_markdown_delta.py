#!/usr/bin/env python3
"""Reject new Markdown lint findings relative to the repository's master branch."""
import collections
import json
import sys


def errors(path):
    with open(path, encoding="utf-8") as handle:
        report = json.load(handle)
    if not isinstance(report, list):
        raise ValueError("markdownlint --json must return a flat diagnostic array")
    counts = collections.Counter()
    for issue in report:
        if not isinstance(issue, dict):
            raise ValueError("invalid Markdown diagnostic")
        name = issue.get("fileName")
        rules = issue.get("ruleNames")
        if not isinstance(name, str) or not isinstance(rules, list) or not rules:
            raise ValueError("missing fileName or ruleNames in Markdown diagnostic")
        counts[(name, rules[0])] += 1
    return counts


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: lint_markdown_delta.py BASELINE CURRENT")
    baseline, current = errors(sys.argv[1]), errors(sys.argv[2])
    new = sorted((key, n - baseline[key]) for key, n in current.items()
                 if n > baseline[key])
    print(f"Markdown violations: baseline={sum(baseline.values())}, "
          f"current={sum(current.values())}")
    for (filename, rule), count in new:
        print(f"NEW {filename}: {rule} +{count}")
    if new:
        raise SystemExit(f"{sum(n for _, n in new)} new Markdown violations")
    print("No Markdown-lint regressions relative to master.")


if __name__ == "__main__":
    main()
