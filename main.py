import numpy as np
from PIL import ImageGrab
import cv2
import time
#from pynput.keyboard import Key, Controller
import threading

import directkeys as k 

keys = k.Keys()

def process_img(original_img):   
    startx, endx, starty, endy = 241, 550, 220, 409
    ball_image = original_img[starty:endy, startx:endx]
    
    hsv = cv2.cvtColor(ball_image, cv2.COLOR_RGB2HSV)
        
    lower_range = np.array([90,200,200])
    upper_range = np.array([120,255,255])

    blue_mask = cv2.inRange(hsv, lower_range, upper_range)
    
    return blue_mask

def screen_record():
    #PressKey(S)
    #i = 0
    #while i <= 5:
    #    time.sleep(1)
    #    i+=1
    #    print(i) 
    #last_time = time.time()
    counter = 0 
    while(True):
        
        printscreen =  ImageGrab.grab(bbox=(0,40,800,640))
        printscreen_array = np.array(printscreen)
        
        mask = process_img(printscreen_array)
        pixels = cv2.countNonZero(mask)
    
        if pixels > 10:
            counter += 1
            #time.sleep(0.3)           
            #keyboard.press(Key.shift)
            #keyboard.press('s')
            #keyboard.press(Key.down)
            #keyboard.release('s')
            #keyboard.release(Key.down)
            #time.sleep(0.03)
            #keyboard.release(Key.shift)
            if counter > 1 and counter < 2:
                print('found')
                keys.directKey("0x53")
                keys.directKey("0x53", keys.key_release)
    
        else:
            counter = 0      

        #print('loop took {} seconds'.format(time.time()-last_time))
        #last_time = time.time()
        #cv2.imshow('window', printscreen)
        #cv2.imshow('mask', mask)
        #cv2.imshow('window2', cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()