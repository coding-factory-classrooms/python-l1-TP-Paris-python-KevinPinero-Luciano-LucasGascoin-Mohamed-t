from os import listdir
from os.path import isfile, join

import cv2
import os
from os.path import basename
from cv2.cv2 import imshow

from filters import gray
from filters import dilate
from filters import blur


#list_imgs = [f for f in listdir("Data/imgs/") if isfile(join("Data/imgs", f))]
#src = ("Data/imgs/img_test.png")

src = ("Data/imgs/img_test.png")

def read_image(src):
    image = cv2.imread(src)
    return image

try:
    output_gray = gray.gray(read_image(src)) # ceci permet de pouvoir ouvrir le fichier ou non
except:
    pass
    #print("le fichieeerezrze")
try:
    output_blur = blur.blur(output_gray, -40)
    output_dilate = dilate.dilate(output_blur, -20)
except:
    pass
    #print(f"le fichier  {src} n'existe pas")


def write():
    try:
        cv2.imwrite(f'output/filtre_{basename(src)}', output_dilate)
    except:
        print(f"le fichier {src} n'est pas une image ou n'existe pas ou vous avez appliqué un flou négatif ou pair")



write()

#test pour afficher l'image si bueno
try:
    cv2.imshow('read', output_dilate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    print(f"le print du test ne fonctionne pas pour {src}")
#-----------------------------------------


# v2.imshow('Dilated Image', dilate_img)


