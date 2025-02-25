# Python Pathlib: A Complete Guide

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Common Operations](#common-operations)
  - [Creating a Path Object](#creating-a-path-object)
  - [Checking if a Path Exists](#checking-if-a-path-exists)
  - [Reading and Writing Files](#reading-and-writing-files)
  - [Iterating Over Directory Contents](#iterating-over-directory-contents)
  - [Finding Files with Glob Patterns](#finding-files-with-glob-patterns)
  - [Working with File Names and Extensions](#working-with-file-names-and-extensions)
- [Advanced Usage](#advanced-usage)
- [Learning Path](#learning-path)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The `pathlib` module in Python provides an object-oriented interface for handling filesystem paths. It is available in Python 3.4 and later, making it easier and more intuitive to manipulate files and directories compared to traditional string-based operations with `os` and `os.path`.

## Installation
`pathlib` is included in Python's standard library, so no additional installation is required. Simply import it into your script:

```python
from pathlib import Path
```

## Getting Started
To use `pathlib`, you create `Path` objects that represent file or directory paths. These objects provide methods for interacting with the filesystem.

## Common Operations

### Creating a Path Object
```python
from pathlib import Path

# Create a Path object
path = Path("my_folder/my_file.txt")
print(path)
```

### Checking if a Path Exists
```python
if path.exists():
    print("Path exists")
else:
    print("Path does not exist")
```

### Reading and Writing Files
```python
# Define a file path
file_path = Path("example.txt")

# Writing to a file
file_path.write_text("Hello, Pathlib!")

# Reading a file
content = file_path.read_text()
print(content)
```

### Iterating Over Directory Contents
```python
path = Path(".")  # Current directory
for item in path.iterdir():
    print(item)
```

### Finding Files with Glob Patterns
```python
# Find all .txt files in the current directory
for file in Path(".").glob("*.txt"):
    print(file)

# Recursively find all Python files
for file in Path(".").rglob("*.py"):
    print(file)
```

### Working with File Names and Extensions
```python
path = Path("my_folder/example.txt")
print(path.name)   # Output: example.txt
print(path.stem)   # Output: example
print(path.suffix) # Output: .txt
print(path.parent) # Output: my_folder
```

## Advanced Usage
- **Handling Symbolic Links**:
  ```python
  if path.is_symlink():
      print("It is a symlink")
  ```
- **Resolving Absolute Paths**:
  ```python
  print(path.resolve())
  ```
- **Creating and Removing Directories**:
  ```python
  new_dir = Path("new_directory")
  new_dir.mkdir(exist_ok=True)
  new_dir.rmdir()
  ```
- **Deleting a File**:
  ```python
  file_path.unlink()
  ```

## Learning Path
To master `pathlib`, follow this learning path:
1. **Basics**: Learn how to create, check, and manipulate paths.
2. **File Handling**: Practice reading, writing, and deleting files.
3. **Directory Operations**: Explore how to list files and folders.
4. **Pattern Matching**: Use `glob()` and `rglob()` for file searches.
5. **Advanced Concepts**: Understand symbolic links, absolute paths, and working with external libraries like `shutil`.
6. **Project Implementation**: Apply `pathlib` in real-world projects like file management scripts or automation tasks.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new examples to add.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

