# -- coding: utf-8 --
def Zadanie_9(n, m, k):
    if n * m > k and ((k % m) or(k % n)):
        print("Да")
    else:
        print("Нет")
