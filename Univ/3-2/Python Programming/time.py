a = int(input("임의의 초(second)를 정수로 입력하세요. : "))
temp = a

hour = temp // 3600
temp = temp % 3600
minute = temp // 60
sec = temp % 60

print(a,"초는", hour,"시간 ",minute,"분 ",sec,"초 입니다.")