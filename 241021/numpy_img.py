import cv2
import numpy as np

L = [ [[0, 0, 0] for j in range(500)] for i in range(500)]
img = np.array(L, dtype=np.uint8)

# def onMouse(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN or (event == cv2.EVENT_MOUSEMOVE and flags & cv2.EVENT_FLAG_LBUTTON):
#         img[y, x] = [0, 0, 255]  # Change the color to red on left button click or drag
#         cv2.imshow('img', img)

def onMouse(event, x, y, flags, param):
    img[:] = 0
    if event == cv2.EVENT_MOUSEMOVE:
        
        cv2.putText(img,f'{x} {y}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
        cv2.imshow('img', img)

cv2.namedWindow('img')
cv2.setMouseCallback('img', onMouse)

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()