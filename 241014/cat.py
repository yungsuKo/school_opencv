import cv2
import numpy as np
cat = cv2.imread('./img/cat.jpg', cv2.IMREAD_COLOR)
cat_lr = cat[:,::-1]
cv2.imshow('cat', cat)
cv2.imshow('cat_lr', cat_lr)



cv2.waitKey(0)
cv2.destroyAllWindows()