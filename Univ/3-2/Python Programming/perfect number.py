for i in range(1, 10001):
    m = []
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            m.append(j)
            sum += j
    if sum == i:
        print("%d은 완전수입니다. %d의 약수 :" % (i, i), m,", 약수의 합 = %d" % sum)