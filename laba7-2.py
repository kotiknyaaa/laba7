import random
while True:
    n=input("Введите кол-во строк: ")
    m=input("Введите кол-во столбцов: ")
    if m.isdigit() and n.isdigit():
        if int(m)!=0 and int(n)!=0:
            n=int(n)
            m=int(m)
            break

sp=[[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        sp[i][j]=random.randint(0,9)

for text in sp:
    print(*text)

for i in range(n):
    mn=99999
    for j in range(m):
        if sp[i][j]<mn:
            mn=sp[i][j]
    sp[i].insert(0,mn)
sp.sort()

for i in range(n):
    sp[i].pop(0)

print("Готовый список: ")
for text in sp:
    print(*text)