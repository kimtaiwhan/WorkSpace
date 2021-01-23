N = int(input(""))
f = list(map(int, input("").split()))
count = 0
for i in f:
    if i == 1:
        continue
    else:
        num = 1
        while True:
            num += 1
            if i == num:
                count += 1
                break
            if i % num == 0:
                break
print(count)