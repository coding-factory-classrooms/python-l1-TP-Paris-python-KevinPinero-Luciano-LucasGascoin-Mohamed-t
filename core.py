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


k = 0   # Compteur permettant de parcourir la liste contant les fichiers

compteur = 0
args = sys.argv
compteur_out = 0


for i in args:
    #print("test for")
    if (i == "-i"):
        bool = True
    compteur = compteur + 1

path_in = args[compteur-3]
print(f"path in = {path_in}")
print(f"compteur= {compteur}")

try:
    list_img = [f for f in listdir(f"{path_in}") if isfile(join(f"{path_in}", f))]     # affiche la liste des images du dossier
except FileNotFoundError as f:
    print(f"Dossier inexistant")
    sys.exit(1)


print(f'list_img = {list_img}')

def read_image():
    full_path = str(f'{path_in}/{list_img[k]}')

    print(f"second k = {k}")
    img = list_img[k]
    imgstr = str(img)
    print("mon img en str = " + imgstr)
    image1 = cv2.imread(full_path)
    #print(f"mon image lu = {image1}")
    return image1

# for o in args:
#     compteur_out = compteur_out +1
#     if (o == '-o'):
#         util_out = args[compteur_out]   # Recuperation du chemin vers le out de l'utilisteur
#         print(f"util_out = {util_out}")


def write(image):
    l = list_img[k]
    #print(f"Je suis dans write avec l = {l}")

    if not os.path.exists(util_out):
        os.mkdir(util_out)

    try:
        #print("test")
        cv2.imwrite(f'{util_out}/{basename(l)}', image)
    except:
        print(f"le fichier {l} n'est pas une image ou n'existe pas ou vous avez appliqué un flou négatif ou pair")



def exe():
    for i in range (len(list_img)):
        global k
        try:
            output_gray = gray.gray(read_image())
            output_blur = blur.blur(output_gray, 217)
            #output_dilate = dilate.dilate(output_gray, 203)
            output_dilate1 = dilate.dilate(output_blur, 23)
            #read_image()
            write(output_dilate1)
            k = k + 1

        except Exception as e :

            print(e)
            k = k + 1

bool = False
compteur =0
exe()


ma_liste =[]
for i, arg in enumerate(args):
    if arg == "-h":
        print('usage: imagefilter')
        print("-h,----help")
        print("-i,--input-dir")
        print("-o,--output-dir")