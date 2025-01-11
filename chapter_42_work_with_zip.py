# working with zip files in python

from zipfile import ZipFile
from pathlib import Path

# create folder
Path("files").mkdir(parents=True, exist_ok=True)

# create files
with open("files/file1.txt", "w") as file:
    file.write("Hello World")
with open("files/file2.txt", "w") as file:
    file.write("Hello World")

# create zip file with rglob - all files in the folder and subfolders   
with ZipFile("files.zip", "w") as zip:
    for path in Path("files").rglob("*.*"):
        zip.write(path)

# create zip file with iterdir - only files in the folder        
with ZipFile("files.zip", "w") as zip:
    for path in Path("files").iterdir():
        zip.write(path)
        
        
# extract zip file
with ZipFile("files.zip", "r") as zip:
    zip.extractall("extract")
    
# extract single file
with ZipFile("files.zip", "r") as zip:
    zip.extract("files/file1.txt", "extract")
    
# extract single file with rename
with ZipFile("files.zip", "r") as zip:
    zip.extract("files/file1.txt", "extract/rename.txt")
    
# delete zip file
Path("files.zip").unlink()

# delete folder with files
for path in Path("extract").rglob("*.*"):
    path.unlink()
    
for path in Path("files").rglob("*.*"):
    path.unlink()

Path("files").rmdir()
Path("extract").rmdir()

