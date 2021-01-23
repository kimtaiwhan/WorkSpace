for i in range(int(input(""))):
    H, W, N = map(int, input().split())
    if N % H == 0:
        a = H * 100
        b = (N // H)
    else:
        a = (N % H) * 100
        b = (N // H + 1)
    print(a + b)

    # N이 H의 배수일 때를 고려하지 않아서 틀림