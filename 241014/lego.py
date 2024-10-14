import cv2
import numpy as np
th = 180
def callb(val):
    global th
    print(val)
    th=val

org = cv2.imread('./img/lego.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('test', org)
cv2.createTrackbar("threshold", "test",0,255,callb )
cv2.setTrackbarPos("threshold", "test", th)

while cv2.waitKey(33)!=27:
    lego = org.copy()
    lego[lego>th] = 255
    lego[lego<=th] = 0
    cv2.imshow('test', lego)
    
cv2.destroyAllWindows()
    

