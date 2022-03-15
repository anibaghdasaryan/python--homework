import random
lst = []
lst_1 = []
lst_2 = []
lst_3 = []
for i in range(800):
    number = random.randint(0,120)
    lst.append(number)
f = open("file.txt","w+")
for a in lst:
    s = str(a) 
    f.write(s+'\n')
f = open("file.txt","r" )   
lines = f.readlines()
for line in lines:
    lst_1.append(line.strip())
lst_2 = 121*[0]
for k in lst_1:
    lst_2[int(k)] = lst_2[int(k)]+1
for t in range(121):
    lst_3 = lst_3+(lst_2[t])*[t]
f1=open("file_sort.txt","w+")
for n in lst_3:
    m = str(n)
    f1.write(m+'\n')
f1.close() 
