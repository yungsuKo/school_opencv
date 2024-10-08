import numpy as np
import cv2
import random as r

B = np.zeros((40, 40),dtype=np.uint8)
W = np.ones((40, 40),dtype=np.uint8) * 255
A = np.block([[W if r.randint(0,1) else B for j in range(10)] for i in range(10)])

cv2.imshow("Org", A)
cv2.imshow("h_flip", A[:, ::-1])

cv2.waitKey(0)
cv2.destroyAllWindows()