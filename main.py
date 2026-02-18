import os
import shutil
from pathlib import Path

def organize_dir(dir):
    '''
    Scan the files in the directory and move
    .pdf files to Documents/
    .jpg files to Images/
    .zip files to Archives/
    
    if these directories don't exist in the target directory
    mkdir them

    :param dir: a directory to be scanned
    '''
    path = Path(dir).expanduser()
    filenames = os.listdir(path)
    for filename in filenames:
        move_file(str(path), filename)

def move_file(dir: str, filename):
    root, ext = os.path.splitext(filename)
    dest = "."
    if ext == ".pdf":
        dest = "Documents"
    elif ext == ".jpg":
        dest = "Images"
    elif ext == ".zip":
        dest = "Archives"
    else:
        print(f"Skipping {filename}...")
        return

    # If dest doesn't exit, make it.
    src_path = f"{dir}/{filename}"
    dest_path = f"{dir}/{dest}"
    if not os.path.isdir(dest_path):
        print(f"Directory {dest} doesn't exist.")
        print("Making the directory...")
        os.mkdir(dest_path)
    
    cmd = f'mv {filename} {dest}'
    print("Running: " + cmd + "...")
    shutil.move(src_path, dest_path)

def main():
    organize_dir('.')

if __name__ == "__main__":
    main()