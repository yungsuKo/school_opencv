import cv2 
import numpy as np
import matplotlib.pyplot as plt

gamma = 1.7
LUT = [np.power(i/255, gamma)*255 for i in range(256)]
LUT = np.array(LUT, dtype='uint8')

print(LUT)



img = cv2.imread('../img/lena.jpg', cv2.IMREAD_GRAYSCALE)
res=LUT[img]
all_ = np.vstack((img, res))
cv2.imshow('all_', all_)
cv2.waitKey(0)
cv2.destroyAllWindows()