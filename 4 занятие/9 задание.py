# -*- coding: utf-8 -*-
n = int(input(""))
n = n - 2
i = 0
j = 1
q = 0
k = 1
z = 2
if n == -1:
    print("1")
else:
    while i < n:
        i += 1
        q = j
        j = j + k
        k = q
        z += j
    print(z)

        
