#Вариант 3
# -*- coding: utf-8 -*-
import math
def Zadanie_8_1():
    def s(x, y):
        g = math.sqrt(x**2 + y**2)
        return g
    B = []
    for i in range(1,3):
        print("Введите катеты", i,"прямоугольного треугольника:")
        a = int(input("Первый катет: "))
        b = int(input("Второй катет: "))
        B.append(s(a, b))
    if B[0] > B[1]:
        print("Гипотенуза 1-ого треугольника больше 2-ого")
    elif B[1] > B[0]:
        print("Гипотенуза 2-ого треугольника больше 1-ого")
    else:
        print("Гипотенузы равны")
    
