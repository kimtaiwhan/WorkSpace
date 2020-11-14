## 함수 선언 부분 ##
def IsPrime(x):
    if x <= 1: # 2보다 작으면 소수가 아님
        return False
    else:
        for i in range(2, x): # 자신을 제외하고
            if ((x % i) == 0): # 약수인지 검사
                return False
    return True

## 메인 코드 부분 ##
m = int(input("시작 값을 입력하세요 : "))
n = int(input("끝 값을 입력하세요 : "))

print("%d부터 %d사이의 소수는 " % (m, n))

for i in range(m, n +1):
    if (IsPrime(i) == True):
        print("%d " % i, end = "")

print("\n입니다.")