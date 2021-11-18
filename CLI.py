import sys

from pathlib import Path
import core
import cv2
# exists *args
# exists **kwargs
from os import listdir
from os.path import isfile, join

#compteur =0
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

