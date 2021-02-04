N = int(input())
fst = 1
i = 1

if N == 1:
    print(1)
else:
    while True:
        fst += 6 * i
        i += 1
        if N <= fst:
            break
    print(i)

# 시간 초과로 틀림
# N이 1일 때를 고려하지 않아서 틀림
# N이 시작 수일 때를 고려하지 않아서 틀림