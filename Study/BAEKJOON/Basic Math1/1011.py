#T = int(input(""))
x, y = map(int, input("").split())
n = 2
while(True):
    if n == 2:
        sum = 4
    else:
        sum = n * (n + 1) // 2 + n * (n - 1) // 2
    if y - x < sum:
        print(y - x)
        break
    if y - x == sum:
        print(2 * n - 1)
        break
    n += 1