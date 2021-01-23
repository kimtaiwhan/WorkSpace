M, N = map(int, input("").split())
a = [False, False] + [True] * (N - 1)
f = []
for i in range(2, N + 1):
    if a[i] == True:
        for j in range(i + i, N + 1, i):
            a[j] = False
        if i >= M:
            print(i)