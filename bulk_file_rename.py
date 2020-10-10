import shutil
import os
from datetime import datetime

def movefiles(path, prefix2):
    list_of_files = os.listdir(path) # returns list
    modified_list_of_files = [prefix2 + fileName for fileName in list_of_files]
    for index in range(len(list_of_files)):
        srcPath = os.path.join(path, list_of_files[index])
        destPath = os.path.join(path, modified_list_of_files[index])
        print("{0}\n".format(destPath))
        if (os.path.isdir(srcPath)):
            shutil.copytree(srcPath, destPath)
            shutil.rmtree(srcPath)
            movefiles(destPath, prefix2)
        elif (os.path.isfile):
            shutil.move(srcPath, destPath)



print("Welcome to the File Renaming exercise program.")
filePath = input("What is the path to the directory you want to bulk rename the contents of? \n")
today = datetime.now()

prefix = today.strftime("%b-%d-%Y-%H%M%S")

if (os.path.isdir(filePath)):
    movefiles(filePath, prefix)





# revert

        
    





