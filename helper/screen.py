import cv2
from PIL import ImageGrab
import numpy as np
from .constants import Constants
import copy

class Screen:
    def __init__(self):
        self.fullscreen = None
        self.screenshot = None
        self.blue_mask = None
        self.play = False

    def processFrame(self):
        self.grab()
        self.updatePitch()
        self.play = self.findPitchMarker()

    def grab(self):
        capture = ImageGrab.grab(
            bbox=(
                Constants.SC_UPPER_LEFT,
                Constants.SC_UPPER_RIGHT,
                Constants.SC_LOWER_LEFT,
                Constants.SC_LOWER_RIGHT
            )
        )
        self.screenshot = np.array(capture)
        self.fullscreen = self.screenshot

    def updatePitch(self):
        pitch = self.screenshot[Constants.PITCH_START_Y:Constants.PITCH_END_Y, Constants.PITCH_START_X:Constants.PITCH_END_X]
        self.screenshot = cv2.cvtColor(pitch, cv2.COLOR_RGB2HSV)

    def findPitchMarker(self):
        pitch = copy.deepcopy(self.screenshot)
        self.blue_mask = cv2.inRange(pitch, Constants.BLUE_LOWER_RANGE, Constants.BLUE_UPPER_RANGE)

        pixels = cv2.countNonZero(self.blue_mask)

        # if pixels > 10 and pixels < 200:
        #     return True
        
        if pixels > 10:
            return True
        
        return False