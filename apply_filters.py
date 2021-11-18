import conditionsF as c
from filters import blur as b
from filters import dilate as d
from filters import gray as g
from CLI import dictionary

dico={
    'input':'',
    'output':'',
    'filtres':'gray, blur',
}

key_f = dico['filtres']


def apply_filters():
    for i in dictionary.keys():
        if i == "blur" & len(key_f) == 1:
            result = b.blur()
            return result
        elif i == "dilate" & len(key_f) == 1:
            result = d.dilate()
            return result
        elif i == "gray" & len(key_f) == 1:
            result = g.gray()
            return result
        elif i == "gray" & i == "blur" & len(key_f) == 2:
            result = c.gray_n_blur()
            return result
        elif i == "blur" & i == "dilate" & len(key_f) == 2:
            result = c.blur_n_dilate()
            return result
        elif i == "gray" & i == "dilate" & len(key_f) == 2:
            result = c.gray_n_dilate()
            return result
        else:
            result = c.all_filters()
            return result