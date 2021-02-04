def factorial(N, ans):
    if N == 1:
        return ans
    else:
        ans *= N
        return factorial(N - 1, ans)

N = int(input())
ans = 1
print(1 if N == 0 else factorial(N, ans))