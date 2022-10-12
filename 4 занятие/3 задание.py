# -- coding: utf-8 --
print("Первое число должно быть больше второго")
A_3 = int(input("Введите первое число "))
B_3 = int(input("Введите второе число "))
if A_3 % 2 ==1:
    print(A_3)
    while A_3 > B_3:
        A_3 -=2
        print(A_3, end=";")
elif A_3 % 2 == 0:
    A_3 -=1
    print(A_3)
    while A_3 > B_3:
        A_3 -=2
        print(A_3, end=";")
