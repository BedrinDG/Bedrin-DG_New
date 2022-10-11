seconds = int(input("Введите число секунд "))
day = seconds // 86400
hour = (seconds - day * 86400) // 3600
minute = (seconds - day * 86400 - hour * 3600) // 60
seconds_1 = seconds - day * 86400 - hour * 3600 - minute * 60
print(seconds, "секунд это", day, "Д.", hour, "Ч.", minute, "М.", seconds_1, "С.")
