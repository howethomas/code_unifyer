import os
import ast
from typing import LiteralString


def traverse_directory(directory) -> LiteralString:
    """
    Traverse a directory and its subdirectories to unify Python code.

    Args:
        directory (str): The root directory of the Python project.

    Returns:
        LiteralString: A string containing the unified Python code.
    """
    unified_code = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                unified_code.append(f"# File: {file_path}\n{content}\n")
    return '\n'.join(unified_code)


def remove_comments_and_docstrings(source_code) -> str:
    """
    Removes comments and docstrings from the given source code.

    Args:
        source_code (str): The source code to remove comments and docstrings from.

    Returns:
        str: The source code with comments and docstrings removed.
    """
    parsed = ast.parse(source_code)
    for node in ast.walk(parsed):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
            if ast.get_docstring(node):
                node.body = node.body[1:]
    return ast.unparse(parsed)


def unify_code_tree(directory, remove_comments=False) -> str | LiteralString:
    """
    Unifies the Python code tree from a given directory.

    Args:
        directory (str): The root directory of the Python project.
        remove_comments (bool, optional): Whether to remove comments and docstrings. Defaults to False.

    Returns:
        str | LiteralString: The unified Python code as a string.
    """
    unified_code = traverse_directory(directory)
    if remove_comments:
        unified_code = remove_comments_and_docstrings(unified_code)
    return unified_code


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Unify Python code tree for LLM analysis")
    parser.add_argument("directory", help="Root directory of the Python project")
    parser.add_argument("--remove-comments", action="store_true", help="Remove comments and docstrings")
    parser.add_argument("--output", help="Output file path (default: unified_code.py)")
    args = parser.parse_args()

    unified_code = unify_code_tree(args.directory, args.remove_comments)
    
    output_file = args.output or "unified_code.py"
    with open(output_file, 'w') as f:
        f.write(unified_code)
    
    print(f"Unified code has been written to {output_file}")
