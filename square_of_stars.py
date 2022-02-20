#square of stars *
numeric=int(input("Введіть цілочисельне число від 5 до 20: "))
i=1
while i <= numeric:
    j = 1
    while j <= numeric:
        print("*", end='\t')
        j = j + 1
    print()
    i = i + 1