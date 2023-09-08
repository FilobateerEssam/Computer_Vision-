# Packegs

import numpy as np
import cv2

#----------- read Image -----------

img = cv2.imread('../images/flemingo.jpg');

print(img)

# know the dimensions of the photo
print(img.shape)

# ----------- Display The Photo -----------

# cv2.imshow('example',img)
#
# cv2.waitKey(10000)
# cv2.destroyAllWindows()

# if value 0 wouldn't close untill press button


cv2.imshow('example',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


#----------- save Image in Differnt or the Same Format -----------

print(cv2.imwrite('./images/example.png',img))