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
dictionnary = {}

k = 0   # Compteur permettant de parcourir la liste contant les fichiers


#list_img = list(p.glob('Data/imgs/*.*'))  # retour console : [PosixPath('Data/imgs/img_test.png')]


compteur = 0    # compteur pour récupérer l'element suivant le -i
args = sys.argv
compteur_out = 0



import configparser


config = configparser.ConfigParser()
print("________________________________________________________")



print("________________________________________________________")






for i in args:
    #print("test for")
    # if (i == "-i"):
    #     bool = True
    compteur = compteur + 1


bool2 = False

path_in = args[compteur-3]
print(f"path in = {path_in}")
print(f"compteur= {compteur}")

dictionnary['input'] = path_in
#print(f'DICTIONNARY = {dictionnary}')
v = 0

try:

    for elem in args:
        v = v + 1
        if (elem == "--config-file"):
            file_ini =  args[v]
            l = config.read(file_ini)
            pathinput_default = config['general']['input_dir']
            pathoutput_default = config['general']['output_dir']
            path_in = pathinput_default
            global util_out
            util_out = pathoutput_default
except Exception:
    print('Argument manquant ou en trop')




try:
    list_img = [f for f in listdir(f"{path_in}") if isfile(join(f"{path_in}", f))]     # affiche la liste des images du dossier
except Exception as f:    #FileNotFoundError -> prend en compte uniquement l'existence des fichiers
    print(f"Dossier inexistant ou erreur d'écriture dans la commande")
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



for o in args:
    compteur_out = compteur_out +1

    print(f"compteur_out = {compteur_out}")
    if (o == '-o'):
#        global util_out
        util_out = args[compteur_out]   # Recuperation du chemin vers le out de l'utilisteur
        dictionnary["output"] = util_out
        print(f"util_out = {util_out}")






print(f"DICTIONNNAIRE = {dictionnary}")


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

        #print('Boucle principal')
        try:

            #print(f"k: {k} ")
            #print('Dans try principal')
            output_gray = gray.gray(read_image())
            # print('entre gray et blur')
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



#bool = False
#compteur =0
exe()
ma_liste =[]


for i, arg in enumerate(args):
    if arg == "-h":
        print('usage: imagefilter')
        print("-h,----help")
        print("-i,--input-dir")
        print("-o,--output-dir")











#test pour afficher l'image si bueno
# try:
#     cv2.imshow('read', output_dilate)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# except:
#     print(f"le print du test ne fonctionne pas pour {src}")
#-----------------------------------------


# v2.imshow('Dilated Image', dilate_img)





