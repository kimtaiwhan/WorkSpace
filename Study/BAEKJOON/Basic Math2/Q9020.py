def isPrime(n):
    a = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if a[i] == True:
            for j in range(i + i, n, i):
                a[j] = False
    return [i for i in range(2, n) if a[i] == True]

def prime(n):
    b = isPrime(n)
    c = max([i for i in range(len(b)) if b[i] <= n / 2])
    for i in range(c, -1, -1):
        for j in range(i, len(b)):
            if b[i] + b[j] == n:
                return [b[i], b[j]]

for i in range(int(input())):
    n = int(input())
    print(" ".join(map(str, prime(n))))

# 몰라서 보고했음