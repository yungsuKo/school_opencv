import numpy as np
import cv2

black = np.zeros((200, 200),dtype=np.uint8)
white = np.zeros((200, 200),dtype=np.uint8) * 255
W, H = 400, 400
width = 20
m,n = W//width, H//width
res=np.block([[black if (i+j)%2==1 else white for j in range(n) ] for i in range(m)])

cv2.imshow("res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 비슷한게 시험에 하나 나올거임ㅋ