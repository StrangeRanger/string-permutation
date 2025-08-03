# String Permutation

[![Project Tracker](https://img.shields.io/badge/repo%20status-Project%20Tracker-lightgrey)](https://hthompson.dev/project-tracker#project-258707884)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This project is designed to take a given word or string of characters and create every possible permutation.

While this isn't a huge project, there are a few things that might need explaining or would be good to know. [Click here](https://github.com/StrangeRanger/string-permutation/wiki) to take a look at the wiki.

## Demo

[![asciicast](https://asciinema.hthompson.dev/a/8.svg)](https://asciinema.hthompson.dev/a/8)

## Features

- **Two permutation types:**
  - Permutation with partial or no repetition
  - Permutation with repetition
- **Flexible output options:**
  - Display permutations on screen
  - Save permutations to a file
- **Duplicate character handling:**
  - Automatic detection of duplicate characters
  - Options to remove duplicates or continue with them
- **Progress tracking:** Real-time progress bar for file operations
- **Cross-platform support:** Works on Windows, macOS, and Linux
- **File size estimation:** Shows approximate output file size before generation

## Getting Started

### Prerequisites

- **Python** 3.7 or higher
- **Optional:** `pipenv` for virtual environment management (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/StrangeRanger/string-permutation
   cd string-permutation
   ```

2. Install dependencies (choose one method):

   **Option A: Global installation**
   ```bash
   python3 -m pip install -r requirements.txt
   ```

   **Option B: Virtual environment (recommended)**
   ```bash
   # Install pipenv if you don't have it
   pip install pipenv

   # Install dependencies in virtual environment
   pipenv install
   ```

## Usage

To execute the program, use one of the following commands:

**If using global installation:**
```bash
python3 string_permutation.py
```

**If using pipenv:**
```bash
pipenv run python string_permutation.py
```

## License

This project is licensed under the [MIT License](LICENSE).
