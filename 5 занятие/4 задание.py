# -*- coding: utf-8 -*-
x = int(input("Введите число x: "))
y = int(input("Введите число y: "))
u = 0
while x < y:
    x = x + (x / 10)
    u += 1
print(u,"Дней")
    
