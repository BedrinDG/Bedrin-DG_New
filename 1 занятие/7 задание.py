number = int(input("Введите любое число, чтобы проверить четное оно или нечетное "))
number_1 = (number % 2)
if number_1 == 0:
    print("Четное")
else:
    print("Нечетное")
