#Вариант 3
# -*- coding: utf-8 -*-
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
A = []
l_1 = 0
k_1 = 0
for i in range(n):
    B = []
    for j in range(m):
        print('Введите [', i,',',j,'] элемент')
        B.append(int(input()))
    A.append(B)
for i in A:
    print(' '.join(list(map(str, i))))
print()
#Нахождение макс значения
p = A[0][0]
for l in range(n):
    for k in range(m):      
        if p < A[l][k]:
            l_1 = l
            k_1 = k
            p = A[l][k]
A[0], A[l_1] = A[l_1],A[0]
A[0][0], A[0][k_1] = A[0][k_1], A[0][0]
for i in A:
    print(' '.join(list(map(str, i))))



    

