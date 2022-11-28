#Вариант 3
# -*- coding: utf-8 -*-
def Zadanie_9_1(n):
    A = []
    o = 0
    for i in range(n):
        B = []
        for j in range(n):
            print('Введите [', i,',',j,'] элемент')
            B.append(int(input()))
        A.append(B)
    for i in range(n):
        for j in range(n):
            if A[i][j] == A[j][i]:
                o += 1
            elif i == j:
                continue
            else:
                break
    if o == n**2:
        print('Матрица симметрична')
    else:
        print('Матрица не симметрична')
        
