# -*- coding: utf-8 -*-
#3 Вариант
n = int(input("Введите длину массива: "))
D = []
summ = 0
p = 0
for i in range(n):
    print("Введите", i,"элемент: ")
    D.append(int(input()))
    p += 1
    if (p%2) != 0:
        summ += D[i]
print("Полученный массив:",D)
print("Сумма чисел с нечётным индексом:",summ)
    
