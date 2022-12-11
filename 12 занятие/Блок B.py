#1 задание
def f():
    s = int(input())
    if s == 0:
        return 0
    return max(s, f())
print(f())
    
