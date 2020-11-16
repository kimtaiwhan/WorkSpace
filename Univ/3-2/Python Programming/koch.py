import turtle

n = int(input("Type recursion depth : "))
t = turtle.Turtle()
leng = 300

def koch(leng, n):
    if n > 0:
        koch(leng / 3.0, n - 1)
        t.left(60)
        koch(leng / 3.0, n - 1)
        t.right(120)
        koch(leng / 3.0, n - 1)
        t.left(60)
        koch(leng / 3.0, n - 1)

    else :
        t.forward(leng)

koch(leng, n)