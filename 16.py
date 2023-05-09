import random
a = input("Qani ismchayizni kiritingchi.Agar meni ismimni tug'ri kirita olsangiz omadli raqam egasi bulasiz😉 :")
c = random.randrange(0,100)
while a.lower() == "munisa":
    b = random.randrange(0, 100)
    print("Meni ismimni topdiz va sizga ", b , " soni taqdim etiladi")
    break

if a.lower() != "munisa":
    print("Qayg'urmang ", a + "jon 🤗 . Sizga ", c , " sonimiz to'g'ri keldi.") 