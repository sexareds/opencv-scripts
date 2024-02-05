import cv2 as cv

img = cv.imread('images/ufc-logo.png')
cv.imshow('UFC Logo', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray UFC Logo', gray)

# blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur UFC Logo', blur)

# edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny UFC Logo', canny)

# dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated UFC Logo', dilated)

# eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded UFC Logo', eroded)


cv.waitKey(0)