import cv2
import logger as f


def gray(image):
    """[function for applying gray filter to image]

        Args:
            image ([file.jpg or .png or .jpeg]): [image]

        Returns:
            [image]: [filtered image with gray filter applied]
    """
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    f.filter_log("grayscale")
    return img_gray
