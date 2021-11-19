from pathlib import Path


def get_images(dir):

    images = []
    dir = Path(dir).glob('**/*.[jpg][png][jpeg]*')
    for i in dir:
        image = str(i)
        images.append(image)
    return images
