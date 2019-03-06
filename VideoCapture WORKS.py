import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from pynput.keyboard import Key, Controller

acc = 1


def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img

commence = input("'start' to commence... ")

def main():
    while 1 == 1:
        if commence == 'start' or 'Start' or 'go' or 'Go':
            global acc
            if acc == 1:
                acc+=1
                time.sleep(3)
                main()


            last_time = time.time()
            while True:
                screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640))) # ROI (Region Of Interest - what pixels are captured)
                print('Frame took {} seconds'.format(time.time()-last_time)) # displays FPS
                last_time = time.time() # Time taken for a frame to be displayed (used to find the FPS)
                new_screen = process_img(screen) # used to display the screen recording
                cv2.imshow('Screen Capture', new_screen) # first parameter is the title, followed by the display of the screen capture
                #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break

main()
                
                
