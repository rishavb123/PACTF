# -*- encoding: utf-8 -*-
#Example
#------------------------------------------------
#w = '\xd7\xe5\xeb\xff\xe1\xe8\xed\xf1\xea'
#print w.decode('cp1251').encode('utf-8')

given = 'необходимая информация'
trying = given.decode('cp1251')
count = 0
t = trying
print len(t)
for x in trying:
    print count
    print x
    count+=1