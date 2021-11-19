import cv2
import logger


def blur(image, intensity):
    img_blur = cv2.GaussianBlur(image, (intensity,intensity), cv2.BORDER_DEFAULT) # à voir si si cela fonctionne intensity
    logger.filter_log("blur")
    return img_blur
