# -*- coding: utf-8 -*-
n = int(input("Введите целое число большее 2: "))
i = 2
if n > 2:
    while i <= n:
        k = n % i
        if k != 0:
            i += 1
        elif k == 0:
            print(i, 'наименьший делитель')
            break
    else:
        print('Это число не делится на цело')
else:
    print("n должно быть > 2")
