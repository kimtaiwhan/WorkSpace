A, B, C = input().split()

if int(B) >= int(C):
    print(-1)

else:
    print((int(A) // (int(C) - int(B))) + 1)

# 시간 초과로 틀림