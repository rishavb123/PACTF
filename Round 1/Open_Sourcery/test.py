from os import walk

i = "PUT THE PATH OF THE CHROMIUM FOLDER HERE"
    

f = []
for (dirpath, dirnames, filenames) in walk(i):
    for filename in filenames:
        f.append(dirpath+"\\"+filename)

        
for x in f:
    file = open(x,"r")
    lines = file.readlines()
    for y in range(len(lines)):
        if("flag" in lines[y]):
            print x+": line "+ str(y+1)
    file.close()