import numpy as np
from PIL import ImageGrab
import cv2
import time
import keyboard as kb
import time
import os

#ALL MOVES => ['shift+s+right+down', 'shift+s+left+down', 
#              'shift+s+down', 'shift+s+right', 'shift+s+left']

training_data = []

file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists! Loading data...')
    training_data = list(np.load(file_name))
else:
    print('Starting from Scratch')    

def process_img(original_img):   
    startx, endx, starty, endy = 241, 550, 220, 409
    ball_image = original_img[starty:endy, startx:endx]
    
    hsv = cv2.cvtColor(ball_image, cv2.COLOR_RGB2HSV)
        
    lower_range = np.array([90,200,200])
    upper_range = np.array([120,255,255])

    blue_mask = cv2.inRange(hsv, lower_range, upper_range)
    
    return blue_mask

def screen_record(): 
    last_time = time.time()
    counter = 0
    key_presses = []
    pictures = []
    while(True):
        printscreen =  ImageGrab.grab(bbox=(0,40,800,640))
        printscreen_array = np.array(printscreen)
        
        mask = process_img(printscreen_array)
        pixels = cv2.countNonZero(mask)
    
        if pixels > 10:
            ##WAIT FOR 12 MORE FRAMES THEN CHECK IF THE USER PRESSES ANY KEY IN ANOTHER 2 SECONDS
            player_move = key_selected()
            pictures.append(mask)
            key_presses.append(player_move)
            counter += 1
             
        else:
            if counter > 0:
                counter = 0
                move_captured = False
                try:
                    for key in key_presses:
                        if key != 'NOTHING':
                            move_captured = True
                except Exception as e:
                    pass 
                
                if move_captured:           
                    final_shot = move_played(key_presses)
                    pic = pictures[len(pictures) - 2]
                    
                    pictures = []
                    key_presses = []
                    
                    print(final_shot)
                    
                    training_data.append([pic, final_shot])
                    
                    #np.save(file_name, training_data)
                    
                    if len(training_data) % 5 == 0:
                        print(len(training_data))
                                                                                                     

        #print('loop took {} seconds'.format(time.time()-last_time))
        #last_time = time.time()
        #cv2.imshow('window', printscreen)
        cv2.imshow('mask', mask)
        #cv2.imshow('window2', cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        
def key_selected():
    if kb.is_pressed('shift+s+right+down'):
        return 'shift+s+right+down'
    
    elif kb.is_pressed('shift+s+left+down'):
        return 'shift+s+left+down'
    
    elif kb.is_pressed('shift+s+down'):
        return 'shift+s+down'
    
    elif kb.is_pressed('shift+s+right'):
        return 'shift+s+right' 
        
    elif kb.is_pressed('shift+s+left'):
        return 'shift+s+left'
    
    else:
        return 'NOTHING' 
    
def move_played(key_presses):
    key_presses_index = len(key_presses) - 1
    
    output = [0,0,0,0,0]
    
    all_moves = ['shift+s+right+down', 'shift+s+left+down', 'shift+s+down', 'shift+s+right', 'shift+s+left']
    
    while key_presses_index >= 0:
        #print('YES!')
        if key_presses[key_presses_index] != 'NOTHING':
            for move in all_moves:
                if key_presses[key_presses_index] == move:
                    i = all_moves.index(move)
                    output[i] = 1
                    return output
                    break  
        
        key_presses_index -= 1          
                
screen_record()