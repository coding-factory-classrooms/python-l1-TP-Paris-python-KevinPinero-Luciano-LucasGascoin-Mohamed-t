import cv2
import logger as f


def dilate(image, intensity):
    kernel = cv2.numpy.ones((intensity, intensity), 'uint8')
    img_dilate = cv2.dilate(image, kernel, iterations=1)
    f.filter_log("dilate")
    return img_dilate
