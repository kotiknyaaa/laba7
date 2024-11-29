import random
while True:
    m=input("Введите кол-во строк: ")
    n=input("Введите кол-во столбцов: ")
    if m.isdigit() and n.isdigit():
        if int(m)!=0 and int(n)!=0:
            n=int(n)
            m=int(m)
            break

sp=[[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        sp[i][j]=random.randint(0,9)

for text in sp:
    print(*text)

while True:
    k=input("Введите число столбца: ")
    if k.isdigit():
        if int(k)<=n and int(k)!=0:
            k=int(k)
            break

print("k-ый столбец:")
for i in range(m):
    print(sp[i][k-1])