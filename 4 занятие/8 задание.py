# -*- coding: utf-8 -*-
def Zadanie_4_8(n):
    if n <= 9:
        for i in range(1, n):
            j = 1
            while i >= j:
                print(j, end="")
                j += 1
            print(end='\n')
        j = 1
        while n >= j:
            print(j, end="")
            j += 1
    else:
        print("n должно быть <= 9")
