import os , sys

list = []

for x in os.listdir(os.getcwd()):
    list.append(x)

count = 0
for j in range(len(list)):
    count = 0
    print list[j]
    try:
        for x in os.listdir(os.getcwd()+"/"+str(list[j])):
            if int(x.split("-")[0]) <= 9:
                temp = x[:8]
            else:
                temp = x[:9]
            try:
                os.rename(  list[j] +"/"+ x, list[j] +"/"+ temp + str(count) + '.txt')
                count =  count + 1
            except:
                continue
    except:
        continue