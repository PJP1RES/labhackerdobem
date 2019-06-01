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

bgcolor("MidnightBlue")

for star in range(30):
    moveToRandomLocation()
    drawStar(randint(5,25), "White")

#use a função para desenhar estrelas!
#drawStar(50, "Blue")
#forward(100)

#drawStar(30, "Yellow")
#left(120)
#forward(150)

#drawStar(70, "Green")

hideturtle()
done()
