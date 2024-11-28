while True:
    n=input("Введите число эл-ов в словаре: ")
    if n.isdigit():
        if int(n)!=0:
            n=int(n)
            break

slovar=dict()
for _ in range(n):
    while True:
        a=input("Введите сначала страну, затем название(я) рек через пробел: ").split()
        if len(a)>=2 and "end" not in a:
            for i in range(1,len(a)):
                slovar[a[i]]=a[0]
        break

while True:
    k=input("Введите название вашей реки, для выхода пропишите 'end': ")
    if k=="end":
        print("Удачки)")
        break
    else:
        if k in slovar:
            print(k, "протекает в", slovar[k], sep=" ")
        else:
            print("Ууупс... Кажется такой реки нету!")