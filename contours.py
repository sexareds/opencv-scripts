import cv2 as cv

img = cv.imread('images/ufc-logo.png')

cv.imshow('UFC Logo', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray UFC Logo', gray)

# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny UFC Logo', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh UFC Logo', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found')

cv.waitKey(0)