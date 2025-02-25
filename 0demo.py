from pathlib import Path

# Find all .txt files in the current directory
txt_files = list(Path(".").glob("*.txt"))
print(txt_files)

# Find all Python files in subdirectories
py_files = list(Path(".").rglob("*.py"))
print(py_files)

# Find all files inside a specific folder
data_files = list(Path("my_folder").glob("*"))
print(data_files)
