#!/usr/bin/env python3

""" Simple move script for dataset """
import os
import shutil #copyfile


if not os.path.exists("./full_test"):
    os.mkdir("./full_test")
    os.mkdir("./full_test/slides")
    os.mkdir("./full_test/frames")

DEST_DIR = "./full_test/"

test_count = 1
ppt_count = 1
for folder in sorted(os.walk('./Dataset')):
    for file in folder[2]:
        file_src = folder[0] + "/" + file
        if 'ppt' in file:
            file_dest = DEST_DIR + "frames/ppt" + str(ppt_count) + '.jpg'
            ppt_count += 1
        else:
            file_dest = DEST_DIR + "frames/" + str(test_count) + '.jpg'
            test_count += 1
        shutil.copyfile(file_src, file_dest)