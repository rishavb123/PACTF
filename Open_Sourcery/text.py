from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(".."):
    for filename in filenames:
        f.append(dirpath+"\\"+filename)
        
for x in f:
    print x