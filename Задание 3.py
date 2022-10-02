# -*- coding: utf-8 -*-
#Задание 1
num_1 = int(input("Введите 1 число "))
num_2 = int(input("Введите 2 число "))
num_3 = int(input("Введите 3 число "))
summ = num_1 + num_2 + num_3
print(summ)
#Задание 2
side_1 = int(input("Введите число "))
side_2 = int(input("Введите число "))
side_3 = int(input("Введите число "))
if side_1 > side_2 and side_1 > side_3:
    square = (1/2 * side_2 * side_3)
    print("Площадь треугольника", square)
elif side_2 > side_1 and side_2 > side_3:
    square = (1/2 * side_1 * side_3)
    print("Площадь треугольника", square)
elif side_3 > side_1 and side_3 > side_2:
    square = (1/2 * side_2 * side_1)
    print("Площадь треугольника", square)
else:
    print("Это точно стороны прямоугольного треугольника?")
#Задание 3
n = int(input("Введите число минут "))
if n > 1440:
    print("Число должно быть в промежутке от 0 до 1440")
else:
    hours = n // 60
    minute = n - hours * 60
    if hours > 23 and minute > 59:
        print("0 часов", "0 минут")
    elif hours > 23:
        print("0 часов", minute, "минут")
    elif minute > 59:
        print(hours, "часов", "0 минут")
    else:
        print(hours, "часов", minute, "минут")
#Задание 4
def Zadanie_4(a, b, l, N):
    length = ((N*2-1)*a)+((N*2-2)*b)+2*l
    if length == 0:
        print("Зачем вам шнурки)")
    else:
        print("Вам нужны шнурки длинной ", length)
#Задание 5
def Zadanie_5(number_1, number_2, number_3):
    if number_1 < number_3 and number_1 < number_2:
        print("Число", number_1, "наименьшее")
    elif number_2 < number_1 and number_2 < number_3:
        print("Число", number_2, "наименьшее")
    elif number_3 < number_1 and number_3 < number_2:
        print("Число", number_3, "наименьшее")
#Задание 6
def Zadanie_6(column_1, line_1, column_2, line_2):
    if (column_1 > 8 or line_1 > 8) or (column_2 > 8 or line_2 > 8):
        print("Это точно шахматная доска?")
    else:
        cell_1=(column_1 + line_1) % 2
        cell_2=(column_2 + line_2) % 2
        if cell_1 == cell_2:
            print("Да")
        else:
            print("Нет")
#Задание 7
def Zadanie_7(years):
    if ((years % 400 == 0)) or ((years % 4 == 0) and not(years % 100 == 0)):
        print("Да")
    else:
        print("Нет")
#Задание 8
def Zadanie_8(x, y, z):
    if x == y == z:
        print("3")
    elif x == y or y == z or z == x:
        print("2")
    else:
        print("0")
#Задание 9
def Zadanie_9(n, m, k):
    if n * m > k and ((k % m) or(k % n)):
        print("Да")
    else:
        print("Нет")

