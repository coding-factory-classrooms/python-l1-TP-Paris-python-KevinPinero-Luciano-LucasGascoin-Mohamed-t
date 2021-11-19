from pathlib import Path


def get_images(dir):
    """
    Fetch all images and put it in a list
    :param dir: path towards images
    :return: images list
    """

    images = []
    dir = Path(dir).glob('**/*.[jpg][png][jpeg]*')
    for i in dir:
        image = str(i)
        images.append(image)
    return images
