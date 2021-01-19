def sig(n):
    if n == 1:
        return 1
    if n == 2:
        return n + 1
    return n * (n - 1) // 2 + sig(n - 1)

for i in range(int(input(""))):
    k = int(input(""))
    n = int(input(""))
    if n == 1:
        num = 1
    elif n == 2:
        num = k + 2
    else:
        num = num + 
#1 5 15 35 70 126 ..
#1 4 10 20 35 56 84
#1 3  6 10 15 21 28