# Packegs

import numpy as np
import cv2

#----------- read Image -----------

img = cv2.imread('../images/bird.jpg') # BGR   (blue,green,red)

def display(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Define A Canvas to draw on it
# row al tol , Columns Al3rd , RGB colors
canvas = np.zeros((300,300,3),dtype="uint8")  # black because it all zeros values

green = (0,255,0)
red = (0,0,255)
blue = (255,0,0)

cv2.rectangle(canvas,(10,10),(60,60),green)
cv2.rectangle(canvas,(200,30),(225,180),green)
                                            #think
cv2.rectangle(canvas,(50,200),(200,225),red,5)
cv2.rectangle(canvas,(200,50),(225,200),blue,-1)

display('Rectangle',canvas)