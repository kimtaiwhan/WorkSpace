# 변수 설정 #
x = float(input("임의의 실수 x를 입력해주세요. : "))
n = int(input("임의의 정수 n을 입력해주세요. : "))
result = 1

# n이 음수 일 때 #
if n < 0:
    for i in range(-n):
        result *= (1 / x)

# n이 0일 때 #
elif n == 0:
    result = 1

# n이 양수 일 때 #
else:
    for i in range(n):
        result *= x

# 출력 #
print("%f의 %d제곱 %f입니다." % (x, n, result))