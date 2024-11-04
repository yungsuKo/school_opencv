import cv2 as cv
import numpy as np

kernel = np.array([[0,1,1,2,2,2,1,1,0],
     [1,2,4,5,5,5,4,2,1],
     [1,4,5,3,0,3,5,4,1],
     [2,5,3,-12,-24,-12,3,5,2],
     [2,5,0,-24,-40,-24,0,5,2],
     [2,5,3,-12,-24,-12,3,5,2],
     [1,4,5,3,0,3,5,4,1],
     [1,2,4,5,5,5,4,2,1],
     [0,1,1,2,2,2,1,1,0]])


img = cv.imread('../img/kbskids.png')

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()