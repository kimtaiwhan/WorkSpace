#1 1 2 3 2 1 1 2 3 4 5 4 3 2 1
#15 - 9 6     3
#6 - 3 3      2
#
#6 - 9 3
#1 2 1 1 2 3 4 3 2 1 1 2 3 4 5

X = int(input())
UpNum = 1
DownNum = 3
n = 1

#1개 3X2-1개 5X2-1개
#(2n + 1)
#(2n) X 2 - 1

if X == 1:
    molecule = 1
    denominator = 1
else:
    while(True):
        if X > UpNum:
            UpNum = UpNum + (2 * n + 1) * 2 - 1
            n += 1
        elif X == UpNum:
            molecule = 1
            break
        else:
            n -= 1
            UpNum = UpNum - ((2 * n + 1) * 2 - 1)
            temp = X - UpNum
            print(temp)
            print(2 * n + 1)
            if temp > 2 * n + 1:
                molecule = temp - (2 * n + 1)
            else:
                molecule = temp
            break

print(molecule)