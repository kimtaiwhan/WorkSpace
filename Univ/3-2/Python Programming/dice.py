import random

dice_A = random.randrange(1, 7)
dice_B = random.randrange(1, 7)

print("A의 주사위 숫자는 %d입니다." % dice_A)
print("B의 주사위 숫자는 %d입니다." % dice_B)

if dice_A > dice_B:
    print("A가 이겼습니다.")

elif dice_A < dice_B:
    print("B가 이겼습니다.")

else:
    print("비겼습니다.")