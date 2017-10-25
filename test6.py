import re

x="my name is mayank mahavar .\n mayank mahavar mayank"
x=x.split()
a={}
for i in x:
    a[i]=x.count(i)
for i in a:
    print i,a[i]

"""
f=open('stem/TRAIN/0.txt','r')
lines=f.read()
print len(lines)
test= re.split(" |'.\n'",lines)
print len(test)
dic={}
for x in test:
    dic[x]=test.count(x)
print len(dic)
for i in dic:
    print i,dic[i]
"""