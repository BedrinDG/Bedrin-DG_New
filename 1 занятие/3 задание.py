# -- coding: utf-8 --
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
