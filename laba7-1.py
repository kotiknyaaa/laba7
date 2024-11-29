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
for i in range(n):
    for j in range(m):
        sp[i][j]=random.randint(0,9)

while True:
    k=input("Введите натуральное чилсо меньше или равное n: ")
    if k.isdigit():
        if int(k)<=int(m):
            k=int(k)
            break

for p in sp:
    print(*p)

print("Элементы k-го столбца ниже:")
for i in range(n):
    print(sp[i][k-1])
