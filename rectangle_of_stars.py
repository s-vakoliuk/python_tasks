#rectangle of stars

a = 10
i = a
while i >= 1:
    if i == a or i == 1:
        j = a
        while j > 0:
            print('*', end='')
            j -= 1
        print()
    else:
        j = a - 2
        print('*', end='')
        while j > 0:
            print(' ', end='')
            j -= 1
        print('*')
    i -= 1