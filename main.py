import turtle

listA = list(map(int, input().split()))
for i in listA:
    turtle.circle(i)
turtle.done()