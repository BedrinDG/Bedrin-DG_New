# -- coding: utf-8 --
def Zadanie_4_5(n):
    n_1 = 0
    for i in range(1, n):
        n_1 = n_1 + i**3
    n_1 = n_1 + n**3
    print(n_1)
