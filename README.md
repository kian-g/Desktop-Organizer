# Desktop Declutter

A small terminal-based Python utility that organizes files in a chosen directory by automatically sorting them into dated folders based on their file extensions.

Example:
If you choose extensions `py` and `txt`, the tool creates folders like:

`py_2025-11-18/`
`txt_2025-11-18/`

Matching files are moved into their respective folders.
If a folder ends up empty, it is automatically removed.

---

## Features

- Interactive terminal menu
- Add any number of file extensions to organize
- Choose any directory to process
- Confirmation prompt before running the organizer
- Creates folders named `<extension>_<date>`
- Moves files into their matching folder
- Automatically deletes empty folders after sorting

---

## Requirements

Install the only dependency:

pip install simple-term-menu

---

## Usage

Run the script:

`python main.py`

You will be presented with a menu:

1. Enter file extensions — Add extensions to sort (e.g., py, txt, jpg)
2. Run — Choose a directory and organize it
3. Quit — Exit the program

### Example flow

> Enter file extension #1: py

> Enter file extension #2: txt

> Enter file extension #3: (press enter to stop)

> Enter directory to organize: ../Desktop

> Will organize this directory: /Users/you/Desktop

> Are you sure you want to run this? You cannot go back.

> Successfully organized 12 files!

> Removed folder /Users/you/Desktop/js_2025-11-18 as it was empty after organization.

---

## Notes

- The script only organizes files whose extensions you explicitly add.
- Existing folders with the same generated name are reused instead of recreated.
