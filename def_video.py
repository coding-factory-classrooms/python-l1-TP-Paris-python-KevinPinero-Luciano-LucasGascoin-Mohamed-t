import cv2
import os
import sys


vidcap = cv2.VideoCapture('/Users/mohamed/Documents/coursCoding/Python/python-l1-TP-Paris-python-KevinPinero-Luciano-LucasGascoin-Mohamed-t/Data/videos/Seoul.mp4')
success, image = vidcap.read()
count = 0
args = sys.argv


def func_vid():

    global  success
    for i in args:
        if (i == "--video"):
            while success:
                global count

                try:
                    if not os.path.exists(f"output"):
                        os.mkdir(f"output")
                except:
                    pass
                try:
                    cv2.imwrite(f"output/image_%d.jpg" % count, image)
                except Exception:
                   # print(f"Erreur de type : {Exception}")
                    pass
                success, image = vidcap.read()
                #print('Saved image ', count)
                count += 1


func_vid()
