def fibonacci(n):
    if n == 0:
        number = 0
    elif n == 1:
        number = 1
    else:
        number = fibonacci(n - 1) + fibonacci(n - 2)

    return number

n = int(input())
print(fibonacci(n))