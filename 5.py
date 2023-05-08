try:
    
    a = input("Anney fayl nomchasini kiriting. faqat shunda ham adashmang mani vaqtimni olib 😂  ")

    f = open(a, "r", encoding="utf-8" )
    print(f.read())
except FileNotFoundError:
    print("Anney aytdimku adashma deb 🤦‍♀️. Ko'zlaringni kattaroq och 😳")
    