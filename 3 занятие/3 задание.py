n = int(input("Введите число минут "))
if n > 1440:
    while n > 1440:
        n = n - 1440
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
