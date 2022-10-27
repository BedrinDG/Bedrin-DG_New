# -*- coding: utf-8 -*-
j = 1
n = 0
f = 0
m = 0
while j != 0:
    j = int(input("Введите неотрицательное число: "))
    if (j > n) and n != 0:
        f +=1
    else:
        f = 1
    if f > m:
        m = f
    n = j
m -= 1
print(m)
