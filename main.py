import core
from os import listdir
from os.path import isfile, join


path = "Data/"
dirs = listdir( path )

print(dirs)

#
# liste_dir = [f for f in listdir("Data/")]
# print(liste_dir)
for i, d in dirs:
    print(i[d])

# for i in :
#     print(i)

#list_imgs = [f for f in listdir(liste_dir) if isfile(join(".", f))]
#path = '/Data/imgs'
#img = "/Data/imgs/"

#print(str(liste_dir))

#FichList = [ f for f in path if isfile(join('.',f)) ]
#print(FichList)
#print(f"hdsjhsqjhdqs {list_imgs}")

# print(path)
# #FichList = [ f for f in path if isfile(join('.',f)) ]
# #print(FichList)
# print(fichiers)



