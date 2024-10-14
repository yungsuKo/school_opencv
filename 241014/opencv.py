import cv2
import numpy as np

img = np.ones((256,256), dtype=np.uint8)*128
img[50:206, 50:206] = 255
cv2.imshow("test", img)
f = lambda x:int(155/255*x)

L = [[[f(j), 127, 50] for j in range(256)] for i in range(256)]
cimg = np.array(L, dtype=np.int8)
cimg[50:206, 50:206] = [0, 50, 255]
cv2.imshow("cimg", cimg)

cv2.waitKey(0)
cv2.destroyAllWindows()