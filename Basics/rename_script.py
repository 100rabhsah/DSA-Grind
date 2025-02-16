import os
import re

# Update with your actual directory path
directory = "/home/dev100rabh/DSA-Grind/Basics/"

# Check if directory exists
if not os.path.exists(directory):
    print(f"Error: Directory '{directory}' does not exist.")
    exit(1)

# Iterate over all files in the directory
for filename in os.listdir(directory):
    match = re.match(r"([a-zA-Z]+)(\d+)(\.py)$", filename)
    if match:
        name, number, extension = match.groups()
        new_name = f"{number}{name}{extension}"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")

print("Renaming complete!")
