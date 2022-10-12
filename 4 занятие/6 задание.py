# -- coding: utf-8 --
n = int(input("Введите число n: "))
N = n + 1
n_1 = 0
n_2 = 1
for i in range(1, N):
        n_2 *= i
        n_1 += n_2
print(n_1)
        
