# -- coding: utf-8 --
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
