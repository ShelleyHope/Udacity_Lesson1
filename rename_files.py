

import os

def rename_files():
    #1. Get file names from folder

    file_list = os.listdir(r"/Users/shelleyandkenny/Downloads/Test")
    print(file_list)

    saved_path = os.getcwd()
    os.chdir(r"/Users/shelleyandkenny/Downloads/Test")

    #2. For each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)        


rename_files()
