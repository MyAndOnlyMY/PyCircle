import turtle

listA = list(map(int, input().split()))
radius_ = 20
for i in listA:
    if i > 200:
        turtle.color("blue")
        turtle.fillcolor("blue")
        turtle.begin_fill()
        turtle.circle(radius_)
        turtle.end_fill()
    else:
        turtle.color("black")
        turtle.circle(i)
turtle.done()