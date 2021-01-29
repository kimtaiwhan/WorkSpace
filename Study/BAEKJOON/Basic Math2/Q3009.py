dot_1_x, dot_1_y = map(int, input().split())
dot_2_x, dot_2_y = map(int, input().split())
dot_3_x, dot_3_y = map(int, input().split())

if dot_1_x == dot_2_x:
    x = dot_3_x
else:
    if dot_1_x == dot_3_x:
        x = dot_2_x
    else:
        x = dot_1_x

if dot_1_y == dot_2_y:
    y = dot_3_y
else:
    if dot_1_y == dot_3_y:
        y = dot_2_y
    else:
        y = dot_1_y

print("{} {}".format(x, y))