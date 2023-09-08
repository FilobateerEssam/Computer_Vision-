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

white = (255,255,255)

centerx,centery = (canvas.shape[1] //2 , canvas.shape[0] //2)

for r in range(0,175,25):
    cv2.circle(canvas,(centerx,centery),r,white)

display('Circle',canvas)