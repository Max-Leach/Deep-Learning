from grabscreen import grab_screen
import cv2
import time



x = 50 # how many frames captured
frameTotalTime = 0

for i in range(x):
    
    timeCounter = time.time()
    screen = grab_screen(region=(50, 20, 800, 600)) # parameters for region of screen
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY) # convert to grey
    #screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB) # convert to colour
    lastFrameTime = time.time()-timeCounter # updating time
    print("Frame ", (i+1), " and it took: ", lastFrameTime, "seconds") # output the time taken to capture a frame
    frameTotalTime = frameTotalTime + lastFrameTime # running total of the time taken to capture i frames
    timeCounter = time.time() # updating time

    
    
    cv2.imshow("Screen capture", screen) # show region captured
    cv2.waitKey(10)

avgFrameTime = frameTotalTime/y # average time per frame = total time for all frames / number of frames
print("Avg Frame time: ", avgFrameTime, "seconds") # output average time per frame

cv2.destroyAllWindows()
