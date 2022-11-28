#Вариант 3
# -*- coding: utf-8 -*-
def Zadanie_8_2(n):
    n += ' '
    b = ''
    q = 0
    a = ''
    def String(b):
        global a
        b.lower()
        r = ''.join(sorted(b.lower()))
        a += ' '
        a +=r
        return(b)
    for i in range(len(n)):
        if n[i] == ' ':
            b = n[q:i]
            q = i+1
            String(b)
    print(a)

    
