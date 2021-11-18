from os import listdir
from os.path import isfile, join
import sys
import cv2
import os
from pathlib import Path
from os.path import basename
from cv2.cv2 import imshow

from filters import gray
from filters import dilate
from filters import blur

args = sys.argv


p = Path('.')

#list_img = list(p.glob('Data/imgs/*.*'))  # retour console : [PosixPath('Data/imgs/img_test.png')]
#print(list_img)
#lulu =str(list_img[0])
#print(lulu)

compteur = 0

for i in args:
    #print("test for")
    if (i == "-i"):
        bool = True
    compteur = compteur +1



path = args[compteur-1]
list_img = [f for f in listdir(f"{path}") if isfile(join(f"{path}", f))]

args = sys.argv



listimgread =[]


k= 0


#list_imgs = [f for f in listdir("Data/imgs/") if isfile(join("Data/imgs", f))]
#src = ("Data/imgs/img_test.png")

#src = ("Data/imgs/img_test.png")

def read_image():

        print(f"second k ={k}")
        img = list_img[k]
        imgstr = str(img)
        image1 = cv2.imread(imgstr)
        print(f"image1 = {image1}")
        print("imgstr = " + imgstr)
        return image1



    #print("le fichieeerezrze")
# try:
#     output_blur = blur.blur(output_gray, -40)
#     output_dilate = dilate.dilate(output_blur, -20)
# except:
#     pass
    #print(f"le fichier  {src} n'existe pas")


def write(image):
    l = list_img[k]
    print(f"Je suis dans write avec l = {l}")
    try:
        cv2.imwrite(f'output/{basename(l)}', image)
    except:
        print(f"le fichier {l} n'est pas une image ou n'existe pas ou vous avez appliqué un flou négatif ou pair")





for i in range (len(list_img)):
    print('Boucle principal')
    try:

        #print(f"k: {k} ")
        print('Dans try principal')
        output_gray = gray.gray(read_image())
        print('entre gray et blur')
        output_blur = blur.blur(output_gray, 217)
        #output_blur1 = blur.blur(read_image(), 211)
        output_dilate = dilate.dilate(output_gray, 203)
        output_dilate1 = dilate.dilate(output_blur, 23)

        #read_image()
        write(output_dilate1)
        k = k + 1
    except Exception as e :
        print(e)
        k = k + 1


#test pour afficher l'image si bueno
# try:
#     cv2.imshow('read', output_dilate)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# except:
#     print(f"le print du test ne fonctionne pas pour {src}")
#-----------------------------------------


# v2.imshow('Dilated Image', dilate_img)



bool = False
compteur =0

ma_liste =[]

for i, arg in enumerate(args):
    if arg == "-h":
        print('usage: imagefilter')
        print("-h,----help")
        print("-i,--input-dir")
        print("-o,--output-dir")




