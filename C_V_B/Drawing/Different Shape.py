# Packegs

import numpy as np
import cv2


def display(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Define A Canvas to draw on it
# row al tol , Columns Al3rd , RGB colors
canvas = np.zeros((300,300,3),dtype="uint8")  # black because it all zeros values


for i in range(0,25):
    radius = np.random.randint(5,200)
    color = np.random.randint(0,256,size=(3,)).tolist()
    pt = np.random.randint(0,300,size=(2,))

    cv2.circle(canvas,tuple(pt),radius,color,-1)

display('Different Shape',canvas)