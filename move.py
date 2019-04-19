#!/usr/bin/env python3

""" Simple move script for dataset """
import os
import shutil #copyfile



for file in sorted(os.walk('Dataset')):

    for frame in file[2]:

        if 'ppt' not in frame:
            shutil.copyfile(file[0]+"/"+frame, "../Data/sample_test/frames/"+file[0].split('/')[1]+"_"+frame)
        else:
            shutil.copyfile(file[0]+"/"+frame, "../Data/sample_test/slides/"+file[0].split('/')[1]+"_"+frame)
