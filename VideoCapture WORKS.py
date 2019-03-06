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
                screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
                #print('Frame took {} seconds'.format(time.time()-last_time))
                last_time = time.time()
                new_screen = process_img(screen)
                cv2.imshow('window', new_screen)
                #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break

main()
                
                
