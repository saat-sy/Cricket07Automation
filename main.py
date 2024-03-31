import cv2
import pyvjoy
import time
from helper.screen import Screen

j = pyvjoy.VJoyDevice(1)
j.reset()
j.data.wAxisX= 0x4000
j.update()
j.data.wAxisY= 0x4000
j.update()

screen = Screen()

while True:
    screen.processFrame()

    if screen.play:
        # GET PREV TIME AND CALCULATE TIME
        # time.sleep
        # PLAY THE GODDAMN SHOT

        print("HIT")
        time.sleep(0.2)
        j.data.wAxisX= 0x8000
        j.update()
        j.data.lButtons = 2
        j.update()
        time.sleep(0.5)
        j.data.lButtons = 0
        j.update()
        j.data.wAxisX= 0x4000
        j.update()
        # time.sleep(0.5)
        

    # cv2.imshow('window', screen.blue_mask)
    # cv2.imshow('mask', screen.screenshot)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break