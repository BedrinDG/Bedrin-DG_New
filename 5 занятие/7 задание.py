# -*- coding: utf-8 -*-
def Zadanie_5_7():
    j = 1
    n = 0
    f = 0
    while j != 0:
        j = int(input("Введите неотрицательное число: "))
        if (j > n) and n != 0:
            f +=1
        n = j
    return f
