# -- coding: utf-8 --
def Zadanie_4_3(A_3,B_3):
    print("Первое число должно быть больше второго")
    if A_3 % 2 ==1:
        print(A_3)
        while A_3 > B_3:
            A_3 -=2
            print(A_3)
    elif A_3 % 2 == 0:
        A_3 -=1
        print(A_3)
        while A_3 > B_3:
            A_3 -=2
            print(A_3)
