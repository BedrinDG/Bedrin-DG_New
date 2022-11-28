# -- coding: utf-8 --
def Zadanie_4_7(n):
        N = n + 1
        n_1 = 0
        n_2 = 1
        for i in range(1, N):
                n_2 *= i
                n_1 += n_2
        return n_1
