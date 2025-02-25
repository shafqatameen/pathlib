from pathlib import Path

# Creating a Path object
path = Path("example.txt")

# Check if the path exists
print(path.exists())  # True or False

# Get absolute path
print(path.resolve())

# Get parent directory
print(path.parent)

# Get file name
print(path.name)

# Get file stem (name without extension)
print(path.stem)

# Get file extension
print(path.suffix)

# Check if it's a file or directory
print(path.is_file())  # True or False
print(path.is_dir())   # True or False

# Creating a directory
dir_path = Path("my_folder")
dir_path.mkdir(exist_ok=True)  # Creates the directory if it doesn't exist

# Deleting a file
path.unlink()  # Uncomment to delete the file

# Iterating through files in a directory
for file in Path(".").iterdir():
    print(file)

#path.touch()  # Creates an empty example.txt file
