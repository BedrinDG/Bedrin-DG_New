# -- coding: utf-8 --
def Zadanie_8(x, y, z):
    if x == y == z:
        print("3")
    elif x == y or y == z or z == x:
        print("2")
    else:
        print("0")
