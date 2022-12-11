#3 Задание
def f(N): 
    if len(N) == 1:
        return N
    return N[-1] + f(N[:-1])
print(f(input()))
