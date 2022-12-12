#Вариант 3
# -*- coding: utf-8 -*-
def Zadanie_10_1(n):
    with open('Bedrin_DG_U-224_1_vvod.txt', 'r+') as f:
        line = f.readlines()
        line = [element.replace ("\n", "").split() for element in line]
       # print(line)
        A = []
        o = 0
        p = 0
        for i in range(n):
            B = []
            for j in range(n):
                kl = ''.join(line[p])
                B.append(kl)
                p +=1
            A.append(B)
        print(A)
        for i in range(n):
            for j in range(n):
                if A[i][j] == A[j][i]:
                    o += 1
                elif i == j:
                    continue
                else:
                    break
    with open('Bedrin_DG_U-224_1_vivod.txt', 'w') as f:
        if o == n**2:
            f.write('Матрица симметрична')
        else:
            f.write('Матрица не симметрична')
