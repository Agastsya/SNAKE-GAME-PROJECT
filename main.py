from turtle import Turtle, Screen

# (STEP-1) MAKING A SNAKE BODY
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
snake_pos = [(-40, 0), (-20, 0), (0, 0)]

for position in snake_pos:
    new_body = Turtle("square")
    new_body.color("white")
    new_body.goto(position)


screen.exitonclick()
