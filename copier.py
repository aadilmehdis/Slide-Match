import os
import shutil

if not os.path.exists("./full_test"):
    os.mkdir("./full_test")
    os.mkdir("./full_test/slides")
    os.mkdir("./full_test/frames")

srcdir="."
dstdir="./full_test/"

imagecount = 0
pptcount = 1
f = open('datasetoutput.txt', "w")
for filename in os.listdir(os.getcwd()+'/Dataset/'):
    for image in os.listdir(str(os.getcwd()+'/Dataset/'+filename)):
        if str(image) == "ppt.jpg":
            shutil.copy2(str(os.getcwd()+'/Dataset/'+filename+'/'+image), str(dstdir+'slides/'+'ppt'+str(pptcount)+'.jpg'))
            pptcount = pptcount + 1
        else:
            shutil.copy2(str(os.getcwd()+'/Dataset/'+filename+'/'+image), str(dstdir+'frames/'+str(imagecount)+'.jpg'))
            imagecount = imagecount + 1
    tempimage = imagecount - 5
    tempppt = pptcount - 1
    for i in range(5):
        f.write(str(tempimage)+'.jpg'+' '+'ppt'+str(tempppt)+'.jpg'+'\n')
        tempimage += 1
