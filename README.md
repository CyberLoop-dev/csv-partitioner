<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0f766e&height=170&section=header&text=CSV%20Partitioner&fontSize=38&fontColor=ffffff" alt="CSV Partitioner header"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=19&duration=2800&pause=900&center=true&vCenter=true&width=820&lines=CSV%20Partitioner%20%E2%80%A2%20Partition%20a%20local%20CSV%20by%20one%20chosen%20column%20while%20preserving%20headers%2C%20input%20row%20order%2C%20and%20a%20manifest%20of%20generated%20files." alt="Animated project title"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/csv-partitioner?style=flat-square" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/csv-partitioner?style=flat-square" alt="Language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/csv-partitioner?style=flat-square" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/csv-partitioner?style=flat-square" alt="Last commit"/></p>

![Project illustration](assets/mark.svg)

## 🔎 Overview
Partition a local CSV by one chosen column while preserving headers, input row order, and a manifest of generated files.

## ✨ Features
- 📄 Splits rows by the exact value in a selected header
- 🧾 Preserves the original header and row order in each partition
- 🧼 Creates filesystem-safe filenames and records original values in manifest.json
- 🛑 Refuses to overwrite existing partition files
- 📦 Uses only the Python standard library

## 🎬 Demo
No hosted demo is published. Run the project locally using the Quick Start command below.

## 🚀 Quick Start
    python -m csv_partitioner examples/people.csv --column region --out partitions

## 🧰 Tech Stack
- Python 3.10+
- csv, pathlib, json, argparse
- unittest

## 🗂️ Folder Structure
    csv_partitioner/cli.py      CSV grouping and command-line interface
    csv_partitioner/__main__.py Module entry point
    tests/test_cli.py            Temporary-file tests
    examples/people.csv         Small sample dataset
    pyproject.toml               Package metadata

## 🛣️ Roadmap
- [ ] Add optional case-insensitive grouping
- [ ] Add a maximum number of partitions guard

## 🤝 Contributing
Issues and pull requests are welcome. Keep changes focused, document behavior, and add a small reproducible example for new features.

## 📄 License
Released under the MIT License. See LICENSE.

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:111827&height=110&section=footer" alt="Animated footer wave"/></p>
