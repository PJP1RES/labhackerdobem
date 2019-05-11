from turtle import *
from random import *

def moveToRandomLocation():
    penup()
    setpos(randint(-400,400), randint(-400,400))
    pendown()

# uma função para desenhar uma estrela
def drawStar(starSize, starColour):
    color (starColour)
    pendown()
    begin_fill()
    for side in range (5):
        left(144)
        forward(starSize)
    end_fill()
    penup()

def drawGalaxy(numberOfStars):
    colors = ["Blue", "White", "Yellow"]
    moveToRandomLocation()

    for star in range(numberOfStars):
        penup()
        left(randint(-180,180))
        forward(randint(5,20))
        pendown()
        drawStar(2, choice(colors))

    
speed(11)

bgcolor("MidnightBlue")

for star in range(30):
    moveToRandomLocation()
    drawStar(randint(5,25), "White")

for galaxy in range(3):
    drawGalaxy(40)


hideturtle()
done()
