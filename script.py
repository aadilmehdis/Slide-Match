import sys
import cv2
import glob
import os
from matplotlib import pyplot as plt
import numpy as np

class SlideMatcher :
    """Match noisy frames with slides"""

    def __init__(self) :
        """Initialize SlideMatcher Class"""

        self.slidesLocation = ''
        self.framesLocation = ''
        self.outputFile = 'output.txt'
        self.slidesData = []
        self.framesData = []
        self.slidesNames = []
        self.framesNames = []
        self.matchedSlides = []
        self.MAX = 1000000

    def inputTaker(self) :
        """Take input from given locations and store in arrays"""

        for slideFile in sorted(glob.glob(self.slidesLocation+'/*.jpg')):
            self.slidesNames.append(slideFile.split('/')[-1])
            imageData = cv2.imread(slideFile)
            self.slidesData.append(imageData)

        for frameFile in sorted(glob.glob(self.framesLocation+'/*.jpg')):
            self.framesNames.append(frameFile.split('/')[-1])
            imageData = cv2.imread(frameFile)
            self.framesData.append(imageData)

    def meanSquareError(self, image_a, image_b):
        """Calculates mean squared error between two images"""

        err = np.sum((image_a.astype("float") - image_b.astype("float")) ** 2)
        err /= float(image_a.shape[0] * image_b.shape[1])
        
        return err

    def matchImages(self):
        """Finds best matching slide with respect to each frame"""

        for frame in self.framesData:
            cur_err = self.MAX
            cur_index = -1
            for i in range(len(self.slidesData)):
                temp = self.meanSquareError(frame, self.slidesData[i])
                if temp < cur_err:
                    cur_err = temp
                    cur_index = i
            self.matchedSlides.append(self.slidesNames[cur_index])

    def outputGiver(self) :
        """Writes output to a file"""

        f = open(self.outputFile, "w")
        for i in range(len(self.framesNames)):
            print(self.framesNames[i]+' '+self.matchedSlides[i]+'\n')
            f.write(self.framesNames[i]+' '+self.matchedSlides[i]+'\n')

        f.close()

    def run(self) :
        """Main Engine of class"""
        
        self.inputTaker()
        self.matchImages()
        self.outputGiver()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print ('Command: python3 <rollno>.py <path/to/slides/directory> <path/to/frames/directory>')
        sys.exit(1)
    S = SlideMatcher()
    S.slidesLocation = str(sys.argv[1]) 
    S.framesLocation = str(sys.argv[2]) 
    S.run() 
