import numpy as np

class Constants:
    # Area of gameplay on the monitor
    SC_UPPER_LEFT = 0
    SC_UPPER_RIGHT = 40
    SC_LOWER_LEFT = 800
    SC_LOWER_RIGHT = 640

    # Pitch
    PITCH_START_X = 241
    PITCH_END_X = 550
    PITCH_START_Y = 220
    PITCH_END_Y = 409

    # Blue marker
    BLUE_LOWER_RANGE = np.array([90,200,200])
    BLUE_UPPER_RANGE = np.array([120,255,255])

    # Default Play Time
    DEF_BALL_TIME = 1.5

    # Magic percentage number
    MAGIC = 0.761904762