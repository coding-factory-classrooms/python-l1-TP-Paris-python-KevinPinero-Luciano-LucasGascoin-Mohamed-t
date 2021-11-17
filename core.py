import cv2
import os
from os.path import basename
from cv2.cv2 import imshow

from filters import gray
from filters import dilate
from filters import blur



src = ("Data/imgs/img_test.png")

def read_image(src):
    image = cv2.imread(src)
    return image

output_gray = gray.gray(read_image(src))
output_blur = blur.blur(output_gray, 35)
output_dilate = dilate.dilate(output_blur, 20)


def write():
    cv2.imwrite(f'output/filtre_{basename(src)}', output_dilate)



write()

#test pour afficher l'image si bueno
cv2.imshow('read', output_dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()
#-----------------------------------------


# v2.imshow('Dilated Image', dilate_img)


