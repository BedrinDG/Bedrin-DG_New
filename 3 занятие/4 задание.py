def Zadanie_4(a, b, l, N):
    length = ((N*2-1)*a)+((N*2-2)*b)+2*l
    if length == 0:
        print("Зачем вам шнурки)")
    else:
        print("Вам нужны шнурки длинной ", length)
