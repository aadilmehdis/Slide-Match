#!/usr/bin/env python3

""" Simple move script for dataset """
import os
import shutil #copyfile


if not os.path.exists("./full_test"):
    os.mkdir("./full_test")
    os.mkdir("./full_test/slides")
    os.mkdir("./full_test/frames")

DEST_DIR = "./full_test/"


for folder in sorted(os.walk('./Dataset')):
    # print(folder[2])
    # print(folder[1])
    # print(folder[0])
    # print()
    # print()
    # for file in folder[2]:
    #     file_src = folder[0] + "/" + file
    #     file_dest = DEST_DIR + "frames/" + 
    #     pass

    # for frame in file[2]:
    #     if 'ppt' not in frame:
    #         shutil.copyfile(file[0]+"/"+frame, DEST_DIR+'frames/'+file[0].split('/')[1]+"_"+frame)
    #     else:
    #         shutil.copyfile(file[0]+"/"+frame, DEST_DIR +"slides"+file[0].split('/')[1]+"_"+frame)