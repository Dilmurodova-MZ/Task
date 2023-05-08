try: 
    a = int(input("a: "))
    b = int(input("b: "))
    c = input("Ishorani kiriting: ")
    try:
        if c == '+':
            d = a+b
        elif c == '-':
            d = a-b
        elif c == '*':
            d = a*b
        elif c == '/':
            d = a/b
        else:
            print("Uchinchi qiymatda ishora kiritishni unutdingiz ")
        print(a,c,b,"=",d)

    except NameError:
        print("Uzgaruvchini nomlanishida xatolik")
    except:
        print("Xatolik bor")
except ValueError:
    print("Dasturingizda qiymatlar bilan bog'liq xatolik bor")

