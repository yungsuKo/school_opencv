import cv2
import numpy as np

logo_o = cv2.imread('./img/kbskids.png')
logo = cv2.resize(logo_o, (0,0), interpolation = cv2.INTER_CUBIC,fx=0.2,fy=0.2)
rows,cols,chs = logo.shape


cv2.imshow('logo', logo)

logo_g = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, bin = cv2.threshold(logo_g,150,255,cv2.THRESH_BINARY)

mask_inv=cv2.bitwise_not(bin)
kbs_fg=cv2.bitwise_and(logo, logo,bin)
cv2.imshow('kbs_fg', kbs_fg)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# while True:
#     ret, frame = cap.read()
#     if ret:
#         cv2.imshow('Frame', frame)
#         if cv2.waitKey(33) == 27:
#             break

cv2.waitKey(0)
cv2.destroyAllWindows()