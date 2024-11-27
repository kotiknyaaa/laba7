import random
while True:
    m=input("Введите кол-во столбцов: ")
    n=input("Введите кол-во строк: ")
    if m.isdigit() and n.isdigit():
        if int(m)!=0 and int(n)!=0:
            n=int(n)
            m=int(m)
            break
sp=[[0]*m for i in range(n)]
count=0

for i in range(n):
    for j in range(m):
        sp[i][j]=random.randint(-3,3)

for k in sp:
    print(*k)

for p in range(m):
    check=True
    for z in range(n):
        if sp[z][p]==0:
            check=False
    if check==True:
        count+=1

print("Кол-во столбцов без нулевого эл-а:", count, sep=" ")