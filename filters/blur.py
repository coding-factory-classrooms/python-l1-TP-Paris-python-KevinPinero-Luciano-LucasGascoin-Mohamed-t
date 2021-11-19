import cv2
import logger


def blur(image, intensity):
    """[function for applying blur filter to image]

        Args:
            image ([file.jpg or .png or .jpeg]): [image]
            intensity ([integer %2 == 1]): [take the number and apply this for set intensity]

        Returns:
            [image]: [filtered image with blur filter applied]
    """
    img_blur = cv2.GaussianBlur(image, (intensity,intensity), cv2.BORDER_DEFAULT) # à voir si si cela fonctionne intensity
    logger.filter_log("blur")
    return img_blur
