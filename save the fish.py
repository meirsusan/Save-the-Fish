import turtle
import time
from random import randint


delay = 0.1
level=0
speed=10.0
# Score
score = 0
image_fishup="/Users/meir/Desktop/Arif-V-216-Recovered1.gif"
image_fishr="/Users/meir/Desktop/06111604_Arif-V-216-Recovered2.gif"
image_fishd="/Users/meir/Desktop/Arif-V-216-Recovered3.gif"
image_fishl="/Users/meir/Desktop/Arif-V-216-Recovered4.gif"
# Set up the screen
wn = turtle.Screen()
wn.title("Save the fish")
wn.bgcolor("royalblue")
wn.setup(width=600, height=600)
wn.tracer(0) 
wn.addshape("/Users/meir/Desktop/379446.gif")

backk = turtle.Turtle()
backk.shape("/Users/meir/Desktop/379446.gif")
backk.goto(0,0)

# Fish
fish = turtle.Turtle()
fish.speed(0)
wn.addshape(image_fishl)

wn.addshape(image_fishr)
wn.addshape(image_fishup)
wn.addshape(image_fishd)
fish.shape(image_fishr)
fish.color("black")
fish.penup()
fish.goto(0,0)
fish.direction = "stop"



# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions for the fish
def go_up():
    if fish.direction != "down":
        fish.direction = "up"

def go_down():
    if fish.direction != "up":
        fish.direction = "down"

def go_left():
    if fish.direction != "right":
        fish.direction = "left"

def go_right():
    if fish.direction != "left":
        fish.direction = "right"
        fish.shape(image_fishr)

def move():
    if fish.direction == "up":
        y = fish.ycor()
        fish.sety(y + 20)
        fish.shape(image_fishup)


    if fish.direction == "down":
        y = fish.ycor()
        fish.sety(y - 20)
        fish.shape(image_fishd)

    if fish.direction == "left":
        x = fish.xcor()
        fish.setx(x - 20)
        fish.shape(image_fishl)

    if fish.direction == "right":
        x = fish.xcor()
        fish.setx(x + 20)
        fish.shape(image_fishr)

# Garbage
trash = turtle.Turtle()
trash.speed(0)
wn.addshape("/Users/meir/Desktop/bottle.gif")
trash.shape("/Users/meir/Desktop/bottle.gif")
trash.color("lightgray")
trash.penup()


# Garbage2
trash1 = turtle.Turtle()
trash1.speed(0)
wn.addshape("/Users/meir/Desktop/pbag.gif")
trash1.shape("/Users/meir/Desktop/pbag.gif")
trash1.color("lightgray")
trash1.penup()

# Garbage 4
trash2 = turtle.Turtle()
trash2.speed(0)
trash2.shape("/Users/meir/Desktop/pbag.gif")
trash2.color("lightgray")
trash2.penup()


# Garbage 4
trash3 = turtle.Turtle()
trash3.speed(0)
trash3.shape("/Users/meir/Desktop/bottle.gif")
trash3.color("lightgray")
trash3.penup()

# Food
yem = turtle.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("red")
yem.penup()
yem.goto(randint(-280,280),randint(-280,280))

def eaten():
	yem.goto(randint(-280,280),randint(-280,280))



def trash_lim():
	trash.goto(randint(-290,290),randint(-290,290))
	for x in range(1,randint(2,359)):
		trash.right(1)
		pass
trash_lim()

def trash1_lim():
	trash1.goto(randint(-290,290),randint(-290,290))
	for x in range(1,randint(2,359)):
		trash1.right(1)
		pass
trash1_lim()

def trash2_lim():
	trash2.goto(randint(-290,290),randint(-290,290))
	for x in range(1,randint(2,359)):
		trash2.right(1)
		pass
trash2_lim()

def trash3_lim():
	trash3.goto(randint(-290,290),randint(-290,290))
	for x in range(1,randint(2,359)):
		trash3.right(1)
		pass
def gameO():
	pen.clear()
	pen.color("black")
	pen.write("Game Over",align="center", font=("Courier", 24, "bold"))
	pen.color("white")



trash3_lim()

# Keyboard 
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")



# Main game loop
while True:

    wn.update()
    speed=speed+0.05
    trash.forward(speed)
    trash1.forward(speed)
    trash2.forward(speed)
    trash3.forward(speed)
    pen.clear()
    pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))


    move()
    # Check if the block has hit the border
    if fish.xcor()>290 or fish.xcor()<-290 or fish.ycor()>290 or fish.ycor()<-290:
        score=0
        speed = 10
        gameO()
        time.sleep(2)
        fish.goto(0,0)
        fish.direction = "stop"
    
    # Check if the Garbage has hit the border
    if trash.xcor()>310 or trash.xcor()<-310 or trash.ycor()>310 or trash.ycor()<-310:
        score = score + 1
        trash_lim()
    if trash1.xcor()>310 or trash1.xcor()<-310 or trash1.ycor()>310 or trash1.ycor()<-310:
        score=score+1
        trash1_lim()
    if trash2.xcor()>310 or trash2.xcor()<-310 or trash2.ycor()>310 or trash2.ycor()<-310:
        score=score+1
        trash2_lim()
    if trash3.xcor()>310 or trash3.xcor()<-310 or trash3.ycor()>310 or trash3.ycor()<-310:
        score=score+1
        trash3_lim()
        
    time.sleep(0.1)
    # Check for a collision with a garbage
    if fish.distance(trash) < 20:
    	fish.goto(0,0)
    	gameO()
    	time.sleep(2)
    	score=0
    	speed=10
    	trash_lim()
    if fish.distance(trash1) < 20:
    	fish.goto(0,0)
    	gameO()
    	time.sleep(2)
    	score=0
    	speed=10
    	trash1_lim()
    if fish.distance(trash2) < 20:
    	fish.goto(0,0)
    	gameO()
    	time.sleep(2)
    	score=0
    	speed=10
    	trash2_lim()
    if fish.distance(trash3) < 20:
    	fish.goto(0,0)
    	gameO()
    	time.sleep(2)
    	score=0
    	speed=10
    	trash3_lim()
    if fish.distance(yem) < 24:
    	eaten()
    	score=score + 100
    	


wn.mainloop()
