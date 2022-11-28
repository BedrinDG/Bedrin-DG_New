# -*- coding: utf-8 -*-
def Zadanie_5_4(x,y):
    u = 0
    while x < y:
        x = x + (x / 10)
        u += 1
    return u
    
