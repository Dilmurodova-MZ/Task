a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in a:
    if x % 2 == 0:
        a.remove(x)
print(a)