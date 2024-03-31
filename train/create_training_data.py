import cv2
import time
import keyboard as kb
import time
import os
import numpy as np
from Cricket07Automation.helper.screen import Screen

NO_KEY_SELECTED = "NO_KEY"
ALL_MOVES = ['shift+s+right+down', 'shift+s+left+down', 'shift+s+down', 'shift+s+right', 'shift+s+left', NO_KEY_SELECTED]
FILE_NAME = os.path.join("train", "data", "raw", "training_data.npz")

trainingDataX = []
trainingDataY = []

def key_selected():
    vector = [0] * len(ALL_MOVES)

    if kb.is_pressed('shift+s+right+down'):
        vector[ALL_MOVES.index('shift+s+right+down')] = 1
    elif kb.is_pressed('shift+s+left+down'):
        vector[ALL_MOVES.index('shift+s+left+down')] = 1
    elif kb.is_pressed('shift+s+down'):
        vector[ALL_MOVES.index('shift+s+down')] = 1
    elif kb.is_pressed('shift+s+right'):
        vector[ALL_MOVES.index('shift+s+right')] = 1  
    elif kb.is_pressed('shift+s+left'):
        vector[ALL_MOVES.index('shift+s+left')] = 1
    else:
        vector[ALL_MOVES.index(NO_KEY_SELECTED)] = 1

    return np.array(vector)

if __name__ == "__main__":
    screen = Screen()
    update = 1

    if os.path.isfile(FILE_NAME):
        print('File exists! Loading data...')
        data = np.load(FILE_NAME)
        trainingDataX = list(data['X'])
        trainingDataY = list(data['Y'])
    else:
        print('Starting from Scratch')

    while True:
        screen.processFrame()
        if screen.play:
            screenshot = screen.fullscreen
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            screenshot = cv2.resize(screenshot, (80, 60))

            trainingDataX.append(screenshot)
            trainingDataY.append(key_selected())

            update += 1
            print("Captured", update, "frames")

            if len(trainingDataY) % 100 == 0:
                print("Collected", len(trainingDataY), "frames")
                np.savez(FILE_NAME, X=trainingDataX, Y=trainingDataY)

            