import cv2
import logger as f


def gray(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    f.filter_log("grayscale")
    return img_gray
