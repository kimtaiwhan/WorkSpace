a = 123456 * 2 + 1
b = [True] * a
for i in range(2, int(a ** 0.5) + 1):
    if b[i] == True:
        for j in range(2*i, a, i):
            b[j] = False

def isPrime(n):
    count = 0
    for i in range(n + 1, n * 2 + 1):
        if b[i] == True:
            count += 1
    print(count)

while True:
    n = int(input())
    if n == 0:
        break
    isPrime(n)