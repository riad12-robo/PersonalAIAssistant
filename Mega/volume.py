import cv2
import time
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    success, img = cap.read()
    print(img.shape)  # Print the image shape for debugging

    if success:
        cv2.imshow("Img", img)
        cv2.waitKey(1)
    else:
        print("Error: Frame not captured!")
        break