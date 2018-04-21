from luhn import *

file = open("cc_leak.txt",'r')

lines = file.readlines()
numbers = []

file.close()


for i in range(len(lines)):
    numbers.append(int(lines[i]))
    
for i in range(len(lines)):
    if(not verify(str(numbers[i]))):
        print lines[i]

