import turtle

screen = turtle.Screen()
screen.bgcolor("white")

onigiri = turtle.Turtle()
onigiri.shape("turtle")
onigiri.color("black")
onigiri.speed(3)

def draw_onigiri():
    onigiri.penup()
    onigiri.goto(-100,-50)
    onigiri.pendown()

    onigiri.begin_fill()
    onigiri.fillcolor("white")

    for _ in range (3):
        onigiri.forward(200)
        onigiri.left(120)
    onigiri.end_fill()

screen.exitonclick()
