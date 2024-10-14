import cv2 
import numpy as np

full = cv2.imread('../img/digits.png', cv2.IMREAD_GRAYSCALE)
digits = [[d for d in np.hsplit(h, 100)] for h in np.vsplit(full, 50)]
cv2.imshow('test', digits[0][0])

cv2.waitKey(0)
cv2.destroyAllWindows()