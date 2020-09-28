import cv2
import numpy as np

my_colors = [[0, 63, 109, 222, 115, 219]]

colors = [[102, 255, 255]]

points = []


def empty(a):
    pass


def get_color(img, my_colors):
    lower = np.array([my_colors[0][0], my_colors[0][2], my_colors[0][4]])
    upper = np.array([my_colors[0][1], my_colors[0][3], my_colors[0][5]])
    mask = cv2.inRange(src=img, lowerb=lower, upperb=upper)
    x, y = getcontours(mask)
    points.append([x, y])
    cv2.circle(end_image, (int(x), int(y)), 8, (colors[0][0], colors[0][1], colors[0][2]), cv2.FILLED)
    cv2.bitwise_and(src1=img, src2=img, mask=mask)


def getcontours(img):
    contour, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for i in contour:
        area = cv2.contourArea(i)
        if area > 200:
            # cv2.drawContours(end_image, i, -1, (0, 255, 0), 5)
            perimeter = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * perimeter, True)
            x, y, w, h = cv2.boundingRect(approx)
            # cv2.rectangle(end_image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    return x + (w * 1.2), y


def draw(points, colors):
    for point in points:
        x = point[0]
        y = point[1]
        cv2.circle(end_image, (int(x), int(y)), 8, (colors[0][0], colors[0][1], colors[0][2]), cv2.FILLED)


cap = cv2.VideoCapture(0)

while True:
    # try:
    success, image = cap.read()
    imgGrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGrey, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 150, 350)
    end_image = image.copy()
    get_color(end_image, my_colors)
    draw(points, colors)
    cv2.imshow('output', end_image)
    cv2.waitKey(1)
    # except:
    #     print('error')
    #     break
