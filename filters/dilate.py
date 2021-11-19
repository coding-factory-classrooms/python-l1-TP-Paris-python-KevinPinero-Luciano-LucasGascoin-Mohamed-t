import cv2
import logger as f


def dilate(image, intensity):
    """[function for applying dilate filter to image]

        Args:
            image ([file.jpg or .png or .jpeg]): [image]
            intensity ([integer]): [take the number and apply this for set intensity]

        Returns:
            [image]: [filtered image with dilate filter applied]
    """
    kernel = cv2.numpy.ones((intensity, intensity), 'uint8')
    img_dilate = cv2.dilate(image, kernel, iterations=1)
    f.filter_log("dilate")
    return img_dilate

