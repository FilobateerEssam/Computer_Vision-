# Packegs

import numpy as np
import cv2

#----------- read Image -----------

img = cv2.imread('../images/flemingo.jpg') # BGR   (blue,green,red)

# # Splitted to Colored
#
# b,g,r = cv2.split(img)
#
# cv2.imshow('colored',img)
# cv2.imshow('b',b)
# cv2.imshow('g',g)
# cv2.imshow('r',r)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# -----------color converter-----------

img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# gray Scale

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


cv2.imshow('image BGR',img)
cv2.imshow('image RGB',img_rgb)
cv2.imshow('image GRAY',img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

print(cv2.imwrite('../images/image RGB.png', img_rgb))
print(cv2.imwrite('../images/image GRAY.png', img_gray))