import cv2 as cv
import numpy as np


def DigitDetection(image_path):

    image = cv.imread(image_path)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    th, threshed = cv.threshold(gray, 100, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)
    morphed = cv.morphologyEx(threshed, cv.MORPH_OPEN, np.ones((2, 2)))


    contours= cv.findContours(morphed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]

    nh, nw = image.shape[:2]
    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)

        if h < 0.3 *nh:
            continue

        cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    #cv.drawContours(image, contours, -1, (0,255,0), 2)



    cv.imshow("image", image)
    cv.waitKey(0)

DigitDetection("first.png")