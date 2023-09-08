# Packegs

import numpy as np
import cv2

#----------- read Image -----------

img = cv2.imread('../images/bird.jpg') # BGR   (blue,green,red)

def display(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# display('bird',img)

#accessing Pixels using Slicing

# access first 100 rows & 100 Columns

corners = img[0:100,0:100]

# display('corners',corners)



# changing the first 100 rows & 100 Columns to Green Color

green = (0,255,0)

img[0:100,0:100] = green


display('Manipulating Color',img)