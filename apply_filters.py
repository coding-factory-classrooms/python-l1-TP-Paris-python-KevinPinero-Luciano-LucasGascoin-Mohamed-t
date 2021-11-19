from filters import blur as b
from filters import dilate as d
from filters import gray as g
from cli import split_filters
from read_image import get_images
import logger as l
import cv2
import os
import errno
from cli import rep

path = rep['output']


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def apply_filters(src, filters):
    for img_path in src:
        image = cv2.imread(img_path)
        name = os.path.basename(img_path)
        l.open_log(img_path)
        for f in filters:
            split = f.split(':')
            filter_name = split[0]
            if filter_name in ["grayscale", "greyscale"]:
                image = g.gray(image)
            elif filter_name == "blur":
                if len(split) > 1 and split[1] != '' and int(split[1]) % 2 != 0:
                    intensity = int(split[1])
                    image = b.blur(image, intensity)
                elif split[1] == '':
                    print("Il manque un argument pour utiliser le filtre de flou")
                else:
                    print("L'intensité du flou doit être impaire et positive")
            elif filter_name == "dilate":
                if len(split) > 1 and split[1] != '':
                    intensity = int(split[1])
                    image = d.dilate(image, intensity)
                else:
                    print("Il manque un argument pour utiliser le filtre dilate")
        make_sure_path_exists(rep['output'])
        output_path = f"{rep['output']}/{name}"
        cv2.imwrite(output_path, image)
        l.save_log(output_path)


apply_filters(get_images(rep['input']), split_filters)