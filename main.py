import turtle

screen = turtle.Screen()
screen.bgcolor("white")

onigiri = turtle.Turtle()
onigiri.shape("turtle")
onigiri.color("black")
onigiri.speed(5)
onigiri.pensize(5)

def draw_onigiri():
    onigiri.penup()
    onigiri.goto(-100,-50)
    onigiri.pendown()

    onigiri.begin_fill()
    onigiri.fillcolor("white")

    for _ in range (3):
        onigiri.forward(250)
        onigiri.circle(25,120)
    onigiri.end_fill()

    onigiri.begin_fill()
    onigiri.fillcolor("black")

    onigiri.penup()
    onigiri.goto(-35,-50)
    onigiri.pendown()
    onigiri.left(90)
    onigiri.forward(100)
    onigiri.right(90)
    onigiri.forward(120)
    onigiri.right(90)
    onigiri.forward(100)

    onigiri.end_fill()

draw_onigiri()

screen.exitonclick()
