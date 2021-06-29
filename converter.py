import os
import sys
from cv2 import imread, imwrite
import shutil
import imghdr # imghdr is a python std lib which will detect image type according to its byte stream. 

def listfiles(rootDir):
    #Remove spaces in the path
    rootDir = rootDir.replace(" ","")

    # check whether the format of the path is vaild:
    if not os.path.exists(rootDir):
        while True:
            rootDir = input("The path is invaild, please check and try again:").replace(" ","")
            if os.path.exists(rootDir):
                break
            else:
                continue
    
    # normalise cases on Windows
    rootDir_normal = os.path.normcase(rootDir)
    if os.path.isabs(rootDir_normal):# if the path is abs, switch to relative path. 
        rootDir_normal = os.path.relpath(rootDir_normal)
    list_dirs = os.walk(rootDir_normal)
    
    # Ask for backup permission 
    while True:
        decision = input("Please confirm whether to backup the current file[Y/N]:")
        if (decision == "Y" or decision == "N"):
            break
        else:
            print("Error, Please select whether to backup using Y for Yes N for No.\n Please try again:\n")
            continue

    #root, dirs'contains, files
    for root, dirs, files in list_dirs:
        for d in dirs:
            print(os.path.join(root,d))
        for f in files:
        # get the filename of photo
            fileid = f.split('.')[0]
            filepath = os.path.join(root,f)
            file_type = imghdr.what(filepath) # using imghdr to check file extension.
            
            # detect format webp
            if file_type == "webp":
                print("fileid=",fileid)
                filepath = os.path.join(root,f)
                try:
                    src = imread(filepath,1)# 1 for colored
                    print("src = ",filepath, src.shape)
                    if decision == "Y":# if we decided to backup, then only the file which needs to be converted will be backuped.
                        new_filepath = os.path.join(root,f+".bk")
                        shutil.copyfile(filepath, new_filepath)
                    os.remove(filepath)
                    imwrite(os.path.join(root,fileid+".png"),src)
                    print("Success!")
                except:# when exception happened: backup the file and remove the orginal one.
                    new_filepath = os.path.join(root, f+".bk")
                    shutil.copyfile(filepath, new_filepath)
                    os.remove(filepath)
                    continue

rootDir = input("Please enter the file path:")
listfiles(rootDir)
