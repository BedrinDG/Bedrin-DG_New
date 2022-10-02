# -*- coding: utf-8 -*-
#1 Задание
print("Курс Основы программирования начался")
#2 Задание
a = int(input("Введите любое число "))
print(a)
#3 Задание
age = int(input("Введите ваш возраст "))
name = input("Введите ваше имя ")
name_1 = {'Иван', 'иван', 'Ваня','ваня', 'ivan', 'Ivan', 'Vanya', 'vanya'}
if name in name_1:
    print("Вы импостер)")
elif age > 0 and age < 75:
    if age >= 16:
        print("Поздравляем вы поступили в ВГУИТ")
    elif age < 16:
        years = 16 - age
        if years == 1:
            print("Сначала нужно окончить школу")
            print("Вам ещё учиться 1 год")
        elif years >= 2 and years <= 4:
            print("Сначала нужно окончить школу")
            print("Вам ещё учиться", years , "года")
        elif years >= 5:
            print("Сначала нужно окончить школу")
            print("Вам ещё учиться", years , "лет")
#4 Задание
seconds = int(input("Введите число секунд "))
day = seconds // 86400
hour = (seconds - day * 86400) // 3600
minute = (seconds - day * 86400 - hour * 3600) // 60
seconds_1 = seconds - day * 86400 - hour * 3600 - minute * 60
print(seconds, "секунд это", day, "Д.", hour, "Ч.", minute, "М.", seconds_1, "С.")
#5 Задание
n = int(input("Введите любое число "))
n_1 = n + n**2 + n**3 + n**4 + n**5
print(n_1)
#6 Задание
x = input("Введите любой x ")
y = input("Введите любой y ")
m = 0
m = x
x = y
y = m
print("Теперь x = ", x, ", а y = ", y)
#7 Задание
number = int(input("Введите любое число, чтобы проверить четное оно или нечетное "))
number_1 = (number % 2)
if number_1 == 0:
    print("Четное")
else:
    print("Нечетное")
input("Нажмите Enter чтобы выйти")


              


    


    

