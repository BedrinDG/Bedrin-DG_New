# -*- coding: utf-8 -*-
#3 Вариант
def Zadanie_6(s):
    n = 0
    l =''
    m =''
    for i in range(len(s)):
        if s[i] =='.':
            m = s[i].replace(s[i],' ')
            l += m
            n += 1
        else:
            l += s[i]
    print(l)
    print(n)
    


