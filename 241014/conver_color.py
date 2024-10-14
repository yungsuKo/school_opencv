import cv2
import numpy as np

cat = cv2.imread('./img/cat.jpg')
cat_g = cv2.cvtColor(cat, cv2.COLOR_BGR2GRAY) 

cat_gc = cv2.cvtColor(cat_g, cv2.COLOR_GRAY2BGR)
h, w = cat_gc.shape[:2]
cv2.circle(cat_gc, (w//2, h//2), 50, (0,0,255), thickness = 5)

cv2.imshow("cat", cat)
cv2.imshow("cat_g", cat_g)
cv2.imshow("cat_gc", cat_gc)
cv2.waitKey(0)
cv2.destroyAllWindows()