import cv2
import keyboard as kb
import os
import numpy as np
from Cricket07Automation.helper.screen import Screen

print("TODO: Check Screen()")

ALL_MOVES = ['shift+s+right+down', 'shift+s+left+down', 'shift+s+down', 'shift+s+right', 'shift+s+left']
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
        return []

    return np.array(vector)

if __name__ == "__main__":
    screen = Screen()
    update = 1

    if os.path.isfile(FILE_NAME):
        print('File exists! Loading data...')
        data = np.load(FILE_NAME)
        print(data)
        trainingDataX = list(data['X'])
        trainingDataY = list(data['Y'])
    else:
        print('Starting from Scratch')

    while True:
        screen.processFrame()
        if screen.play:
            screenshot = screen.fullscreen
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            screenshot = cv2.resize(screenshot, (227, 227))

            key = key_selected()
            if len(key) > 0:
                trainingDataX.append(screenshot)
                trainingDataY.append(key)
                update += 1
                print("Captured", update, "frames")

            if update % 10 == 0:
                print("Collected", len(trainingDataY), "frames")
                np.savez(FILE_NAME, X=trainingDataX, Y=trainingDataY)

            