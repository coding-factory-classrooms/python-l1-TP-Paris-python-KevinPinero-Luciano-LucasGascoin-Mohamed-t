import sys
# exists *args
# exists **kwargs

args = sys.argv

dictionary = {}
for strParam in sys.argv[1:]:
    dictionary[strParam] = 'value'
    #dictionary |= {strParam}
    #dictionary = {'key': strParam.values()}


print(dictionary)














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

























