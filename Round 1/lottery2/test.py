from grapher import *

file = open("numbers.txt",'r')

lines = file.readlines()
numbers = []

minimum = 0
maximum = 4294967295

for i in range(len(lines)):
    numbers.append(float(lines[i]))
    
differences = []
double_differences = []

for i in range(1, len(numbers)):
    differences.append(numbers[i]-numbers[i-1])
    
for i in range(1, len(differences)):
    double_differences.append(differences[i]-differences[i-1])
    
divided = []

for i in range(1, len(numbers)):
    divided.append(numbers[i]/numbers[i-1])
    
min_nums = []
    
for i in range(len(numbers)):
    min_nums.append(numbers[i]-min(numbers))

#graph(range(10),numbers[-10:])
#show()

graph(range(1000), numbers)
show()
