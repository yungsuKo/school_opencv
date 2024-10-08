import numpy as np
import cv2 
import random as r

img1 = np.array([[v for v in range(256)] for y in range(256)], dtype=np.uint8)
cv2.imshow("img", img1) # 수평 그라이언트

img2 = np.array([[y for v in range(256)] for y in range(256)], dtype=np.uint8)
cv2.imshow("v", img2) # 수직 그라디언트

f = lambda x: 255 if x>255 else x
img3 = np.array([[f(y+v) for v in range(256)] for y in range(256)], dtype=np.uint8)
cv2.imshow("img3", img3)


cv2.waitKey(0)
cv2.destroyAllWindows()