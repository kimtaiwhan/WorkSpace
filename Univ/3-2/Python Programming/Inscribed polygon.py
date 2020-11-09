import turtle as t

def draw(L):
    t.up()
    t.goto(L, 0)
    t.left(90)
    t.down()
    t.circle(L)
    for N in range(3, 13):
        t.circle(L, 360, N)
    
while True:
    L = float(input("원의 반지름 L을 입력하세요 : "))
    if L <= 0:
        print("0보다 큰 정수를 입력하세요.\n")
    else:
        break

draw(L)