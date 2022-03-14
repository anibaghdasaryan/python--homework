import random
i = 0
lst = []
while i <1000000000:
    number = random.randint(0,120)
    lst = lst + [number]
    i = i+1
print(lst)    
f = open("file.txt","wt")
for a in lst:
    s = str(a) 
    f.write(s+';')
f.close()    
