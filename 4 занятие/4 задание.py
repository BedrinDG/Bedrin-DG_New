# -- coding: utf-8 --
N = int(input("Введите количество чисел "))
n = 0
for i in range(1, N):
    n += i
n += N
print(n)
