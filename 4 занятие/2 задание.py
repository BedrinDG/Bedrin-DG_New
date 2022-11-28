# -- coding: utf-8 --
def Zadanie_4_2(A_2,B_2):    
    if A_2 < B_2:
        B_2 +=1
        for i_2 in range(A_2, B_2):
            print(i_2, end=";")
    elif A_2 > B_2:
        print(A_2)
        while A_2 > B_2:
                A_2 -=1
                print(A_2)
    else:
        print("Числа равны")

