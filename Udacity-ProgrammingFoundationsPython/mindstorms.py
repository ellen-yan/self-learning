import turtle # allows us to draw stuff

def draw_square(direction):
    ellie = turtle.Turtle()
    ellie.setheading(direction)
    ellie.shape("turtle")
    ellie.color("white", "blue")
    ellie.speed(10)

    for i in range(0, 4):
        ellie.forward(100) # 100 pixels forward
        ellie.right(90) # turn 90 degrees

def draw_circle():
    moomoo = turtle.Turtle()
    moomoo.shape("triangle")
    moomoo.color("white", "green")
    moomoo.circle(100) # draw circle of radius 100

def draw_triangle():
    ranger = turtle.Turtle()
    ranger.setpos(40, 40)
    ranger.shape("square")
    ranger.color("white", "black")
    ranger.speed(3)
    for i in range(0, 3):
        ranger.forward(100)
        ranger.right(120)

def draw_circle_from_squares(angle):
    for i in range(0, 360, angle):
        draw_square(i)


window = turtle.Screen()
window.bgcolor("red")
draw_circle_from_squares(5)
#draw_square()
#draw_circle()
#draw_triangle()
window.exitonclick()
