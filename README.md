# ALU Regex Data Extraction (Python)

A simple, beginner-friendly Python script that reads raw text data, extracts specific patterns using regular expressions (regex), and sorts them into a clean JSON output.

## Features
* **Rwandan Phone Numbers:** Automatically detects formats like `+250 795...`, `+250-788...`, and tightly packed formats.
* **ALU Emails:** Automatically scans and organizes accounts into `official`, `alumni`, and `scholar_system` blocks.
* **Credit Card Security:** Finds 16-digit payment card layouts and automatically masks the first 12 digits for safety.
* **XSS Detection:** Scans for dangerous HTML scripts and reports an unsafe system warning flag if found.

## Project Structure
* `input/raw-text.txt` - Your messy system .log
* `src/main.py` - The main Python processing script.
* `output/sample-output.json` - The finalized clean data file.
