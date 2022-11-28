# -*- coding: utf-8 -*-
def Zadanie_5_6():
    n = 0
    w = 1
    r = 0
    while w != 0:
        w = int(input("Введите неотрицательное число: "))
        r += w
        n += 1
    n -=1
    print("Среднее арифметическое = ", r / n)

