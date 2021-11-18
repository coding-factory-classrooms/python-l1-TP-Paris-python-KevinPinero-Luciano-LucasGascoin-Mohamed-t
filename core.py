from os import listdir
from os.path import isfile, join

import cv2
import os
from pathlib import Path
from os.path import basename
from cv2.cv2 import imshow

from filters import gray
from filters import dilate
from filters import blur



p = Path('.')
list_img = list(p.glob('Data/imgs/*.*'))  # retour console : [PosixPath('Data/imgs/img_test.png')]
print(list_img)
#lulu =str(list_img[0])
#print(lulu)



listimgread =[]


k= 0


#list_imgs = [f for f in listdir("Data/imgs/") if isfile(join("Data/imgs", f))]
#src = ("Data/imgs/img_test.png")

#src = ("Data/imgs/img_test.png")
def read_image():
    try:
        print(f"second k ={k}")
        img = list_img[k]
        imgstr = str(img)
        image1 = cv2.imread(imgstr)
        print("imgstr = "+imgstr)
        return image1
    except:
        pass


    #print("le fichieeerezrze")
# try:
#     output_blur = blur.blur(output_gray, -40)
#     output_dilate = dilate.dilate(output_blur, -20)
# except:
#     pass
    #print(f"le fichier  {src} n'existe pas")


def write(image):
    l = list_img[k]
    try:
        cv2.imwrite(f'output/{basename(l)}', image)
    except:
        print(f"le fichier {l} n'est pas une image ou n'existe pas ou vous avez appliqué un flou négatif ou pair")





for i in range (len(list_img)):
    try:
        print(f"k: {k} ")
        output_gray = gray.gray(read_image())
        output_blur = blur.blur(output_gray, 217)
        #output_blur1 = blur.blur(read_image(), 211)
        output_dilate = dilate.dilate(output_gray, 203)
        output_dilate1 = dilate.dilate(output_blur, 23)

        #read_image()
        write(output_dilate1)
        k = k + 1
    except:
        k = k + 1
        pass

#test pour afficher l'image si bueno
# try:
#     cv2.imshow('read', output_dilate)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# except:
#     print(f"le print du test ne fonctionne pas pour {src}")
#-----------------------------------------


# v2.imshow('Dilated Image', dilate_img)


