a = int(input("Listda nechta son qatnashadi: "))
listcha = []
yigindi = 0
k = 0


for x in range(0,a):
    b = input("List qiymatlarini kiriting ketma-ketlikda: ")
    listcha.append(b)
    print(listcha)

for x in listcha:
    yigindi+= int(x)
    k+=1
print("Yig'indi: ", yigindi)

urtacha = yigindi/k
print("O'rtacha qiymati: ", urtacha)