import csv
import tempfile
import unittest
from pathlib import Path
from csv_partitioner.cli import partition_csv

class PartitionerTests(unittest.TestCase):
    def test_splits_rows_and_writes_manifest(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "input.csv"
            source.write_text("name,region\nAda,west\nLin,east\nGrace,west\n", encoding="utf-8")
            result = partition_csv(source, "region", root / "out")
            self.assertEqual(len(result["partitions"]), 2)
            west = root / "out" / "west.csv"
            with west.open(encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual([row["name"] for row in rows], ["Ada", "Grace"])
            self.assertTrue((root / "out" / "manifest.json").exists())

    def test_refuses_to_overwrite(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "input.csv"
            source.write_text("region\nwest\n", encoding="utf-8")
            out = root / "out"
            out.mkdir()
            (out / "west.csv").write_text("keep", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                partition_csv(source, "region", out)

if __name__ == "__main__":
    unittest.main()
