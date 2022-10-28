# -*- coding: utf-8 -*-
#3 Вариант
D = []
for i in range(8):
    print("Введите",i,"элемент")
    D.append(int(input()))
    if D[i] < 15:
        D[i] = D[i] * 2
print("Полученный массив:",D)
