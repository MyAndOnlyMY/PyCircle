import turtle

listA = list(map(int, input().split()))
for i in listA:
    if i==max(listA):
        turtle.color("red")
    else:
        turtle.color("black")
    turtle.circle(i)
turtle.done()