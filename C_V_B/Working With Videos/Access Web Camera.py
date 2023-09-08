# Packages

import  numpy as np
import cv2
import time

#-------------Load Video-------------

# 0 Mean the default camera of mine
cap = cv2.VideoCapture(0) # will use Indexing 0 , 1 , 2
fps = 0
while True :

    start_time = time.time() # start time
    # ret opened or not , frame images
    ret , frame = cap.read()

    #End of the Video , Problem of the Video
    if ret == False:
        break

    # put text in the Video format for inetger   position on the Video
    cv2.putText(frame,'FPS: {: .0f}'.format(fps),(30,40),
                #     Font              Scale    Color     Size
                cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),1)

    cv2.imshow('video',frame)

    # 1 mean load a max frame
    if cv2.waitKey(1) == ord('q'):
        break

    time_taken = time.time() - start_time # time taken in Seconds End Time
    fps = 1 / time_taken # frames per seconds
cap.release()
cv2.destroyAllWindows()