# GitHub Activity CLI

This is a simple command-line tool for fetching a GitHub user's public activities. You can view recent events like push requests, pull requests, and more directly from your terminal.

## Table of Contents
- [About](#about)
- [Setup](#setup)
- [Commands](#commands)
- [Testing](#testing)
- [Acknowledgments](#acknowledgments)

## About

The `GitHub Activity CLI` is a Python-based command-line tool that allows users to fetch and view a GitHub user's public activities. The activities include events like pushes, pull requests, issues, etc.

- **Fetch** recent public events from a GitHub user
- **Display** event type, timestamp, and repository name
- **Run** with a single command:
  ```bash
  github-activity <username>
  ```

## Setup

To run the GitHub Activity CLI application, you'll need to set up your environment and ensure Python is installed.

### Prerequisites

- Python 3.8 or higher
- `pip` package manager (comes with Python)
- Access to the command line or terminal

### 1. Install Python (if not already installed)

- **Windows**: [Download Python](https://www.python.org/downloads/)
- **macOS**: Use Homebrew or download from [Python's official website](https://www.python.org/downloads/).
- **Linux**: Install via package manager, e.g., `sudo apt install python3`.

### 2. Clone the Repository

```bash
git clone https://github.com/bykplx1/GitHub-User-Activity
cd GitHub-User-Activity
```

### 3. Install Dependencies

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install typer requests
```

### 4. Install the Application as a CLI Tool

To make the app available globally from the terminal:

```bash
pip install -e .
```

Now you should be able to run:

```bash
github-activity <username>
```

## Commands

### 1. Fetch User's Activity

To view a GitHub user's public activity, run the following command:

```bash
github-activity <username>
```

Example:

```bash
github-activity torvalds
```

### 2. Error Handling

If the username is invalid or the API fails, the tool will display an error message.

---

## Testing

This project uses Python’s `pytest` and `unittest.mock` modules for testing.

### 1. Running Tests

To run all tests, use the following command in the terminal:

```bash
pytest
```

### 2. Tests for Scenarios

- **Invalid username**: Simulates a 404 response from the GitHub API for non-existent users.
- **API failure**: Simulates network errors or server failures during the API call.

---

## Acknowledgments

This project idea was inspired by [GitHub User Activity - Roadmap.sh](https://roadmap.sh/projects/github-user-activity). Special thanks to the author for sharing the concept!

