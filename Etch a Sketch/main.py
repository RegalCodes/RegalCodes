from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backward():
    tim.backward(10)


def move_left():
    tim.left(90)
    tim.forward(10)

def move_right():
    tim.right(90)
    tim.forward(10)

def clear_all():
    tim.reset()

tim.shape("turtle")

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_all)
screen.exitonclick()