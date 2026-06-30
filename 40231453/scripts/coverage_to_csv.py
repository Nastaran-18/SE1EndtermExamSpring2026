"""
Converts the coverage.py JSON report into a CSV report
(file, statements, missed, coverage_percent) as required by the CI step.
"""

import csv
import json
import sys


def main(json_path: str = "coverage.json", csv_path: str = "coverage.csv") -> None:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    rows = []
    for filename, info in data["files"].items():
        summary = info["summary"]
        rows.append(
            {
                "file": filename,
                "statements": summary["num_statements"],
                "missed": summary["missing_lines"],
                "coverage_percent": round(summary["percent_covered"], 2),
            }
        )

    totals = data["totals"]
    rows.append(
        {
            "file": "TOTAL",
            "statements": totals["num_statements"],
            "missed": totals["missing_lines"],
            "coverage_percent": round(totals["percent_covered"], 2),
        }
    )

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["file", "statements", "missed", "coverage_percent"]
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {csv_path} with {len(rows)} rows.")


if __name__ == "__main__":
    json_path = sys.argv[1] if len(sys.argv) > 1 else "coverage.json"
    csv_path = sys.argv[2] if len(sys.argv) > 2 else "coverage.csv"
    main(json_path, csv_path)
