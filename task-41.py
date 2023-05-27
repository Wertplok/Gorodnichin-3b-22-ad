import os


try:
    os.mkdir('my_folder')
    print("Folder created")
except FileExistsError:
    print("Folder already exists")
