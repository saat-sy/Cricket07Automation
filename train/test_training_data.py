import os
import numpy as np
import cv2

inputFolder = input("Enter the input folder: ")
inputFilename = input("Enter the input filename: ")

FILE_NAME = os.path.join("train", "data", inputFolder, inputFilename)

data = np.load(FILE_NAME)
X = data['X']
Y = data['Y']

for x, y in zip(X, Y):
    cv2.imshow("Win", x)
    print(y)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break