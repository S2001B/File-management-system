# File-management-system
A little file management system for the Libre Office package
# File Management System for LibreOffice

## Overview

This File Management System (FMS) is designed to organize LibreOffice documents by their file extensions. It automatically sorts files into predefined directories, making file management more accessible and more efficient.

## Usage

There are two ways to use the FMS:

1. **Terminal Argument Method**:
   Run the script with the file name as an argument.
python main_system_terminal_argument.py filename.extension

Replace `filename.extension` with your actual file name and extension.

2. **Input Method**:
Simply run the script and input the filename when prompted.
python main_system_input_argument.py

## Functions

- `move()`: Moves a file to the appropriate directory based on its file extension.
- `copy()`: Copies a file to the appropriate directory.
- `sort_files()`: Sorts all files in the root directory into their respective folders based on the extension.

## Requirements

- Python 3.x
- `os` and `shutil` libraries (standard with Python)

## Contributing

Contributions to the File Management System are welcome! Please fork the repository and submit a pull request with your changes.
