import sys

from pathlib import Path
import core
import cv2
# exists *args
# exists **kwargs
from os import listdir
from os.path import isfile, join


dictionary = {}
for strParam in sys.argv[1:]:
    dictionary[strParam] = 'value'
    #dictionary |= {strParam}
    #dictionary = {'key': strParam.values()}


print(dictionary)

for i in dictionary.keys():
    if i == "-h":
        print('usage: imagefilter')
        print("-h,----help")
        print("-i,--input-dir")
        print("-o,--output-dir")
from os.path import basename


args = sys.argv

for i in dictionary.keys():
    if i == "-i":
        print("-i, Data/imgs")


for i in dictionary.keys():
    if i == "-o":
        print("-o, /output")















## -------------------- TESTS -------------------

# ------------------- arg parse --------------
# import argparse
#
#
# parser = argparse.ArgumentParser()
# parser.add_argument("args")
# args = parser.parse_args(write(read_image(lister())))
# print(args)


# return data
# print("Bad  value: %s" % param, file=sys.stderr)

# print(param)

# accumulator += param
# except ValueError:
#     pass
# print( "Bad parameter value: %s" % strParam, file=sys.stderr )


# for i, arg in enumerate(args):
#     if arg == "-h":
#         print('usage: imagefilter')
#         print("-h,----help")
#         print("-i,--input-dir")
#         print("-o,--output-dir")





#!/usr/bin/python3
# -*- coding: utf-8 -*-



# if len( sys.argv ) == 1:
#     print( "Adder by KooR.fr - V1.0" )
#     print( "\tusage: python3 adder.py intValue..." )
#     exit()
#























bool = False
compteur =0

ma_liste =[]

# for i, arg in enumerate(args):
#     if arg == "-h":
#         print('usage: imagefilter')
#         print("-h,----help")
#         print("-i,--input-dir")
#         print("-o,--output-dir")
#
#
#
#
#
# for i in args:
#     #print("test for")
#     if (i == "-i"):
#         bool = True
#     compteur = compteur +1
#
#
# try:
#
#     path = args[compteur-1]
#     list_imgs = [f for f in listdir(f"{path}") if isfile(join(f"{path}", f))]
# except:
#
#     pass
#
#
# if bool:
#
#
#     try:
#         for i in list_imgs:
#             print(f"i = {i}")
#             ls = f"{path}/{i}"
#             ma_liste.append(ls)
#             with open(ls):
#                 print(args[1])
#                 print(args)
#
#                 print('bool vérifié')
#                 print(f"compteurup = {compteur}")
#
#                 p = Path('.')
#                 l = args[compteur - 1]  # Récupération du lien vers le dossier
#                 l_str = str(l)
#                 print(l_str)
#                 ph_str = ls
#                 liste_imgCLI = ma_liste #list(p.glob(ph_str))
#                 print(liste_imgCLI)
#
#
#                 def read_imageCLI():
#
#                     print(f'Etat du dossier : {ma_liste}')
#
#                     if len(ph_str) != 0:
#                         print("Je passssssssssssssssssssssssssssssssssssssssssssssssssssssssssssse en haut ")
#
#                         print(f'len de ph_str = {len(ma_liste)}')
#                         try:
#                             print(f"second k ={core.k}")
#                             img = ph_str[core.k]
#                             imgstr = str(img)
#                             image1 = cv2.imread(imgstr)
#                             print("imgstr = " + imgstr)
#                             return image1
#                         except:
#                             pass
#                     else:
#                         print("Je passssssssssssssssssssssssssssssssssssssssssssssssssssssssssssse en bas ")
#                         pass
#
#
#                 def write_CLI(image):
#                     print("Je suis dans le write")
#                     if len(ma_liste) != 0:
#
#                         l = ph_str[core.k]
#                         try:
#                             cv2.imwrite(f'output/{basename(l)}', image)
#                         except:
#                             print(
#                                 f"le fichier {l} n'est pas une image ou n'existe pas ou vous avez appliqué un flou négatif ou pair")
#                     else:
#                         pass
#
#
#                 for i in range(len(liste_imgCLI)):
#                     try:
#                         print(f"k: {core.k} ")
#                         output_gray = core.gray.gray(read_imageCLI())
#                         output_blur = core.blur.blur(output_gray, 217)
#                         # output_blur1 = blur.blur(read_image(), 211)
#                         output_dilate = core.dilate.dilate(output_gray, 203)
#                         output_dilate1 = core.dilate.dilate(output_blur, 23)
#
#                         # read_image()
#                         print("Test : juste avant appel write")
#                         write_CLI(output_dilate1)
#                         core.k = core.k + 1
#                     except:
#                         core.k = core.k + 1
#                         pass
#
#
#
#     except IOError:
#             print(' Erreur! Le  fichier nexiste pas')
#
#
