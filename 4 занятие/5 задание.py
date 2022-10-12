# -- coding: utf-8 --
n_1 = 1
n = int(input("Введите любое число "))
for i in range(1, n):
    n_1 *= i
n_1 *= n
print(n_1)
