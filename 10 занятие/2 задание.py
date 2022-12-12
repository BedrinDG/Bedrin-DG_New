#Вариант 3
# -*- coding: utf-8 -*-
def Zadanie_10_2(n,m):
    with open('Bedrin_DG_U-224_1_vvod.txt', 'r+') as f:
        line = f.readlines()
        line = [element.replace ("\n", "").split() for element in line]
        A = []
        p = 0
        l_1 = 0
        k_1 = 0
        for i in range(n):
            B = []
            for j in range(m):
                kl = ''.join(line[p])
                B.append(kl)
                p +=1
            A.append(B)
        print(A)
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
    with open('Bedrin_DG_U-224_2_vivod.txt', 'w') as f:
        for i in A:
            f.write('\n')
            f.write(' '.join(list(map(str, i))))

        
