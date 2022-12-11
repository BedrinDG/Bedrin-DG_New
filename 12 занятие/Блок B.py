def f(n):
    s = int(input())
    if s == 0:
        return 0
    elif n == 1 or n%2!=0:
        return s,f(n+1) 
    return f(n+1)
print(f(1))
    
