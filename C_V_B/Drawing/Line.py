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

# draw a green Line

green = (0,255,0)
cv2.line(canvas,(0,0) , (300,300) , green)
# display('canvas with green line',canvas)

#draw a x lines
cv2.line(canvas,(300,0) , (0,300) , green)
cv2.line(canvas,(0,0) , (300,300) , green)

display('canvas with green line',canvas)

#draw a star of Lines
white = (255,255,255)
cv2.line(canvas,(0,0) , (300,300) , white)
cv2.line(canvas,(150,0) , (150,300) , white)
cv2.line(canvas,(0,150) , (300,150) , white)
cv2.line(canvas,(300,0) , (0,300) , white)
display('canvas with green line',canvas)

# print(cv2.imwrite('../images/star.png',canvas))