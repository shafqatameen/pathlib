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

# Use Path.rglob() to find all files
all_files = list(Path(".").rglob("*"))
print(all_files)

# Search for all .py files in the current directory (non-recursive)
for file in Path(".").glob("*.py"):
    print(file,"")
print()

# Search for all .py files in the current directory and subdirectories (recursive)
for file in Path(".").rglob("*.py"):
    print(file)