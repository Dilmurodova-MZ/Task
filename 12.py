a = int(input("Listda nechta son qatnashadi: "))
listcha = []
juftlar = 0
toqlar  = 0


for x in range(0,a):
    b = input("List qiymatlarini kiriting ketma-ketlikda: ")
    listcha.append(b)
    # print(listcha)
    
for y in listcha:
    if int(y) % 2 == 0:
       juftlar += int(y)
    else:
        toqlar += int(y)
print("Juft sonlar yig'indisi: ", juftlar)
print("Toq sonlar yig'indisi: ", toqlar)