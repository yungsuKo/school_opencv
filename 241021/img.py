import cv2

org = cv2.imread('./img/snake.jpg')
img = cv2.resize(org, (0,0), interpolation=cv2.INTER_CUBIC, fx=0.5, fy=0.5)
cv2.imshow('img', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

_, bin = cv2.threshold(gray, 150, 255, cv2.THRESH_OTSU)
cv2.imshow('bin', bin)

bin_c = cv2.cvtColor(bin, cv2.COLOR_GRAY2BGR)
h, w, c = bin_c.shape
cv2.putText(bin_c, "Snake", (w//2, h//2), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0,0), 5)

cv2.imshow('bin_c', bin_c)

cv2.waitKey(0)
cv2.destroyAllWindows()
