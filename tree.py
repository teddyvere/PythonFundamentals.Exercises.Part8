import os
from pathlib import Path

def list_files(directory):
    # Convert the directory string to a Path object
    dir_path = Path(directory)

    # Open the output file once before the loop
    with open("file1.txt", 'w') as output_file:
        # Iterate over each item in the directory
        for item in dir_path.iterdir():
            if item.is_file():
                # Write each file's name to the output file
                output_file.write(f'{item.name}\n')

# Specify the directory
directory = os.path.dirname(os.path.abspath(__file__))

# Call the function
list_files(directory)











