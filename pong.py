import turtle   # Import from the turtle library
import os       # To simplify the programming process and remove the need to rewrite the Os

# Draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=1150, height=720)
screen.tracer(0)

# Draw paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-500, 0)

# Draw paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(500, 0)

# Draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.50
ball.dy = 0.50

# Score
score_1 = 0
score_2 = 0

# Head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 290)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))

# Paddle 1 movement up
def paddle_1_up():
    y = paddle_1.ycor()
    if y < 300:
        y += 30
    else:
        y = 300
    paddle_1.sety(y)

# Paddle 1 movement down
def paddle_1_down():
    y = paddle_1.ycor()
    if y > -300:
        y += -30
    else:
        y = -300
    paddle_1.sety(y)

# Paddle 2 movement up
def paddle_2_up():
    y = paddle_2.ycor()
    if y < 300:
        y += 30
    else:
        y = 300
    paddle_2.sety(y)

# Paddle 2 movement down
def paddle_2_down():
    y = paddle_2.ycor()
    if y > -300:
        y += -30
    else:
        y = -300
    paddle_2.sety(y)


# Keyboard
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

while True:
    screen.update()

    # Ball movement

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Collision with the upper wall
    if ball.ycor() > 350:
        os.system("bounce.wav&")
        ball.sety(350)
        ball.dy *= -1

    # Collision with lower wall
    if ball.ycor() < -350:
        os.system("bounce.wav&")
        ball.sety(-350)
        ball.dy *= -1

    # Collision with left wall
    if ball.xcor() < -500:
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        os.system("258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx = 0.5

    # Collision with right wall
    if ball.xcor() > 500:
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        os.system("258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx = 0.5

    # Collision with paddle 1
    if ball.xcor() < - 497 and paddle_1.ycor() + 70 > ball.ycor() > paddle_1.ycor() - 70:
        ball.dx *= -1.25

        os.system("bounce.wav&")

    # Collision with paddle 2
    if ball.xcor() > 497 and paddle_2.ycor() + 70 > ball.ycor() > paddle_2.ycor() - 70:
        ball.dx *= -1.25
        os.system("bounce.wav&")

