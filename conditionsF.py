from filters import gray as g
from filters import blur as b
from filters import dilate as d
from core import read_image


def all_filters():
    first = b.blur(read_image())
    second = g.gray(first)
    result = d.dilate(second)
    return result


def gray_n_blur(intensity):
    first = g.gray(read_image())
    result = b.blur(first, intensity)
    return result


def gray_n_dilate(intensity):
    first = g.gray(read_image())
    result = d.dilate(first, intensity)
    return result


def blur_n_dilate(intensityb,intensityd):
    first = b.blur(read_image(),intensityb)
    result = d.dilate(first,intensityd)
    return result