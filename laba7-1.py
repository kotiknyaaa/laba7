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
        sp[i][j]=i+j+2

for k in sp:
    print(*k)

for text in range(len(sp)):
    print("Сумма эл-ов строки номер", str(text+1)+":", sum(sp[text]), sep=' ')