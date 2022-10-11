# -- coding: utf-8 --
def Zadanie_5(number_1, number_2, number_3):
    if number_1 < number_3 and number_1 < number_2:
        print("Число", number_1, "наименьшее")
    elif number_2 < number_1 and number_2 < number_3:
        print("Число", number_2, "наименьшее")
    elif number_3 < number_1 and number_3 < number_2:
        print("Число", number_3, "наименьшее")
