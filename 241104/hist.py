import cv2
import numpy as np

def genBigImg(simg):
  im = cv2.resize(simg,(400,400),interpolation=cv2.INTER_AREA)*36
  rows,cols=simg.shape
  for r in range(rows):
    for c in range(cols):
        r0,r1,c0,c1=100*r,100*(r+1),100*c,100*(c+1)
        color= (255,255,255) if simg[r,c]<4 else (0,0,0)
        cv2.putText(im,f'{simg[r,c]}',(c0+40,r0+60),cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
          color,1,cv2.LINE_AA)
  return im

small=np.array([[0,1,1,1], [1,3,1,6],[5,6,6,6],[2,4,4,3]],dtype=np.uint8)
big=genBigImg(small)

cv2.imshow('small Image', small)
cv2.imshow('big Image', big)
cv2.waitKey(0)
cv2.destroyAllWindows()