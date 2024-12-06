while True:
    n = input("Введите число эл-ов в словаре: ")
    if n.isdigit():
        if int(n) != 0:
            n = int(n)
            break
slovar = dict()

for _ in range(n):
    while True:
        a = input("Введите название страны и через запятую городов: ")
        if len(a.split()) >= 2 and ("end" not in a or "end," not in a):
            strana=(a.split()[0])
            count=1
            for i in a:
                if i!=" ":
                    count+=1
                else:
                    break
            a=a[count:]
            a=a.split(", ")
            for i in a:
                slovar[i]=strana
            break

while True:
    z=input("Напишите название вашего города, для выхода пропишите 'end': ")
    if z in slovar:
        print("Город",z,"находится в",slovar[z],sep=" ")
    elif z == "end":
        print("Удачки)")
        break
    else:
        print(" ")