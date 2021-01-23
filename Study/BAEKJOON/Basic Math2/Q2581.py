M = int(input(""))
N = int(input(""))
count = 0
sum = 0
for i in range(M, N + 1):
    if i == 1:
        continue
    else:
        num = 1
        while True:
            num += 1
            if i == num:
                count += 1
                if count == 1:
                    min = i
                sum += i
                break
            if i % num == 0:
                break
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)