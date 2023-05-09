soni = int(input("Nechta son kiritmoqchisiz: "))
listcha = []
for x in range(0, soni):
    a = int(input("Juft son kiriting: "))
    
    if a % 2 == 0:
        listcha.append(a)
        print(listcha)
    else:
        print("Faqat juft son kiriting aynanay :) ")