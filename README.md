# Python Code Tree Unifier

This Python script traverses a directory containing Python code files, combines their contents into a single unified source, and prepares it for analysis by an LLM (Large Language Model). It's particularly useful for presenting an entire codebase to an AI model for review or analysis.

## Features

- Recursively traverses a directory to find all Python (.py) files
- Combines the content of all Python files into a single output file
- Optionally removes comments and docstrings from the unified code
- Allows specification of output file name
- Provides command-line interface for easy use

## Requirements

- Python 3.x

## Installation

1. Clone this repository or download the `code_unifier.py` script.
2. Ensure you have Python 3.x installed on your system.

## Usage

Run the script from the command line with the following syntax:

```
python code_unifier.py <directory> [--remove-comments] [--output <output_file>]
```

### Arguments

- `<directory>`: The root directory of your Python project (required)
- `--remove-comments`: Optional flag to remove comments and docstrings from the unified code
- `--output <output_file>`: Optional argument to specify the output file name (default: unified_code.py)

### Examples

1. Basic usage:
   ```
   python code_unifier.py /path/to/your/python/project
   ```

2. Remove comments and specify output file:
   ```
   python code_unifier.py /path/to/your/python/project --remove-comments --output unified_output.py
   ```

## Output

The script will generate a single Python file containing all the code from the specified directory and its subdirectories. Each file's content in the unified output is preceded by a comment indicating its original path.

## Customization

You can modify the script to add more features, such as:
- Excluding certain directories or files
- Adding more code processing options
- Integrating directly with an LLM API for immediate analysis

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/howethomas/python-code-tree-unifier/issues) if you want to contribute.

## License

This project is licensed under the MIT License.

## Contact

Thomas McCarthy-Howe

Email: ghostofbasho@gmail.com
Twitter: @howethomas

Project Link: [https://github.com/howethomas/python-code-tree-unifier](https://github.com/howethomas/python-code-tree-unifier)
