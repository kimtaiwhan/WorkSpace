X = int(input())
floor, start = 1, 1
while start + floor <= X:
    start += floor
    floor += 1
num = X - start
x, y = num + 1, floor - num
if floor % 2 == 0:
    print('{}/{}'.format(x, y))
else:
    print('{}/{}'.format(y, x))

# 몰라서 보고했음