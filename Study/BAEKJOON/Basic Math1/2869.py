a, b, v = input("").split()
A, B, V = int(a), int(b), int(v)

day = (V - B) / (A - B)
if day == int(day):
    print(int(day))
else:
    print(int(day) + 1)

# 시간 초과로 틀림