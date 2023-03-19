import os
import shutil

# Set the source and destination directories
src_dir = r'C:\01_PythonCodes\Gr8\PythonTermux'
dst_dir = r'C:\01_PythonCodes\Gr8\Insta\New folder'

# Get a list of all the files in the source directory
files = os.listdir(src_dir)

# Loop through each file in the source directory
for file in files:
    # Check if the file is a PNG image
    if file.endswith('.png'):
        # Construct the full file paths
        src_file = os.path.join(src_dir, file)
        dst_file = os.path.join(dst_dir, file)

        # Copy the file from the source directory to the destination directory
        shutil.copy(src_file, dst_file)