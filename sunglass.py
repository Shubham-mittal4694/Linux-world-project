import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, main_img = cap.read()
cap.release()
if not ret or main_img is None:
    print("Error: Unable to capture image from camera.")
    exit()

overlay_img = cv2.imread('sunglasses.png', cv2.IMREAD_UNCHANGED)
if overlay_img is None:
    print("Error: Unable to load overlay image.")
    exit()

overlay_x = 80
overlay_y = 20

overlay_height, overlay_width, _ = overlay_img.shape
y_end = overlay_y + overlay_height
x_end = overlay_x + overlay_width

if y_end > main_img.shape[0]:
    overlay_img = overlay_img[:-(y_end - main_img.shape[0]), :, :]
    y_end = main_img.shape[0]
if x_end > main_img.shape[1]:
    overlay_img = overlay_img[:, :-(x_end - main_img.shape[1]), :].copy()
    x_end = main_img.shape[1]

alpha = overlay_img[:, :, 3] / 255.0
for c in range(0, 3):
    main_img[overlay_y:y_end, overlay_x:x_end, c] = (1 - alpha) * main_img[overlay_y:y_end, overlay_x:x_end, c] + alpha * overlay_img[:, :, c] * 0.5

cv2.imshow('Result', main_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
