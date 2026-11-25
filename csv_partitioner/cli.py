from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


def safe_name(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip()).strip("-.")
    return cleaned[:64] or "blank"


def partition_csv(source: Path, column: str, output: Path) -> dict[str, object]:
    with source.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("Input CSV has no header row")
        if column not in reader.fieldnames:
            raise ValueError(f"Column {column!r} not found; available: {', '.join(reader.fieldnames)}")
        groups: dict[str, list[dict[str, str]]] = {}
        for row in reader:
            groups.setdefault(row.get(column, "") or "", []).append(row)
        headers = reader.fieldnames

    output.mkdir(parents=True, exist_ok=True)
    used: set[str] = set()
    manifest_rows = []
    writes = []
    for value, rows in groups.items():
        base = safe_name(value)
        filename = base + ".csv"
        suffix = 2
        while filename in used:
            filename = f"{base}-{suffix}.csv"
            suffix += 1
        used.add(filename)
        destination = output / filename
        writes.append((destination, rows))
        manifest_rows.append({"value": value, "file": filename, "rows": len(rows)})

    manifest_path = output / "manifest.json"
    collisions = [str(path) for path, _ in writes if path.exists()]
    if manifest_path.exists():
        collisions.append(str(manifest_path))
    if collisions:
        raise FileExistsError("Refusing to overwrite: " + ", ".join(collisions))

    for destination, rows in writes:
        with destination.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)
    manifest = {"source": source.name, "column": column, "partitions": manifest_rows}
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Split a CSV into one file per distinct value in a column.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--column", required=True)
    parser.add_argument("--out", type=Path, default=Path("partitions"))
    args = parser.parse_args()
    try:
        result = partition_csv(args.input, args.column, args.out)
    except (OSError, ValueError, csv.Error) as error:
        parser.exit(2, f"Error: {error}\n")
    print(f"Created {len(result['partitions'])} partition(s) in {args.out}")
    for item in result["partitions"]:
        print(f"  {item['file']}: {item['rows']} row(s) for {item['value']!r}")

if __name__ == "__main__":
    main()
