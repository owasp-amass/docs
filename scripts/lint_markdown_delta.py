#!/usr/bin/env python3
"""Fail on new Markdown lint violations relative to the repository's master branch."""
import collections
import json
import sys


def errors(path):
    with open(path, encoding="utf-8") as handle:
        report = json.load(handle)
    if not isinstance(report, dict):
        raise ValueError("markdownlint JSON must map filenames to diagnostics")
    counts = collections.Counter()
    for filename, diagnostics in report.items():
        if not isinstance(diagnostics, list):
            raise ValueError(f"invalid markdownlint diagnostics for {filename}")
        for issue in diagnostics:
            names = issue.get("ruleNames", [])
            if not names:
                raise ValueError(f"diagnostic missing ruleNames: {filename}")
            counts[(filename, names[0])] += 1
    return counts


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: lint_markdown_delta.py BASELINE CURRENT")
    baseline, current = errors(sys.argv[1]), errors(sys.argv[2])
    new = sorted((key, count - baseline[key]) for key, count in current.items()
                 if count > baseline[key])
    print(f"Markdown violations: baseline={sum(baseline.values())}, "
          f"current={sum(current.values())}")
    for (filename, rule), amount in new:
        print(f"NEW {filename}: {rule} +{amount}")
    if new:
        raise SystemExit(f"{sum(n for _, n in new)} new Markdown violations")
    print("No Markdown-lint regressions relative to master.")


if __name__ == "__main__":
    main()
