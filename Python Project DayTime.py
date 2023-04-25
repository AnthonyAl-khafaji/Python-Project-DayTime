import turtle
from turtle import Screen
screen = Screen()
screen.setup(1200, 800,)
#draw sun
def sunny():
    #Local Varibles
    sun = turtle.Turtle()
    screen.bgcolor("light sky blue")
    sun.speed(0)
    #draw sun
    sun.fillcolor('gold')
    sun.color('gold')
    sun.penup()
    #sun location
    sun.goto(290, 220)
    sun.pendown()
    sun.begin_fill()    
    sun.circle(40)
    sun.end_fill()
    #flare location
    sun.penup()
    sun.goto(230, 276) #60 difference in x 56 in y
    sun.pendown()
    sun.fillcolor('gold')
    sun.begin_fill()
    #draw sunflares
    for i in range(13):
        sun.forward(120)
        sun.right(150)
        #hide turtle
        sun.ht()
    sun.end_fill()
    sun.color('black')
    sun.write("Hurray Your Day Is Sunny\n\tLets Build A Castle!\t \t\t ", align="right", font=("Arial", 14, "bold", "italic"))
    
#draw grass    
def grass():
    #Local Varibles
    grass = turtle.Turtle()
    #set speed
    grass.speed(0)
    #draw grass
    grass.penup()
    #grass start location
    grass.goto(-1000, 20)
    grass.color('green')
    grass.pendown()
    grass.begin_fill()
    grass.forward(2000)
    grass.right(90)
    grass.forward(600)
    grass.right(90)
    grass.forward(2000)
    grass.forward(600)
    grass.right(90)
    grass.fillcolor('green')
    grass.end_fill()
    #hide turtle
    grass.ht()
    
def river():
    #Local Varibles
    river = turtle.Turtle()
    #set speed
    river.speed(0)
    river.penup()
    #river start location
    river.goto(-700, -280)
    river.color('brown')
    river.pendown()
    river.begin_fill()
    #angle to offset circle to line
    river.left(36)
    river.fillcolor('midnight blue')
    #loop to draw river edge
    for i in range(20):
        river.speed(0)
        for i in range(7):
            river.forward(5)
            river.right(10)
        for i in range(7):
            river.forward(5)
            river.left(10)
    #angle to offset circle to line
    river.left(88)
    river.forward(30)
    river.left(90)
    #loop to draw return river edge
    for i in range(20):
        river.speed(0)
        for i in range(7):
            river.forward(5)
            river.right(10)
        for i in range(7):
            river.forward(5)
            river.left(10)
    river.end_fill()       
    turtle.done()
def cloud():
    #Local Varibles
    cloud = turtle.Turtle()
    #set speed
    cloud.speed(0)
    cloud.penup()
    #circle 1 location
    cloud.goto(-400, 280)
    cloud.color('white')
    cloud.pendown()
    cloud.begin_fill()
    cloud.circle(20)
    cloud.end_fill()
    cloud.fillcolor('white')
    cloud.penup()
    #circle 21 location
    cloud.goto(-340, 280)
    cloud.color('white')
    cloud.pendown()
    cloud.begin_fill()
    cloud.circle(20)
    cloud.end_fill()
    cloud.fillcolor('white')
    cloud.penup()
    #circle 3 location
    cloud.goto(-370, 280)
    cloud.color('white')
    cloud.pendown()
    cloud.begin_fill()
    cloud.circle(40)
    cloud.end_fill()
    cloud.fillcolor('white')
    cloud.penup()
    #circle 4 location
    cloud.goto(-320, 300)
    cloud.color('white')
    cloud.pendown()
    cloud.begin_fill()
    cloud.circle(25)
    cloud.end_fill()
    cloud.fillcolor('white')
    cloud.penup()
    #circle 5 location
    cloud.goto(-420, 300)
    cloud.color('white')
    cloud.pendown()
    cloud.begin_fill()
    cloud.circle(25)
    cloud.end_fill()
    cloud.fillcolor('white')
    #hide turtle
    cloud.ht()

def main():
    #Call
    #Local Varibles
      sunny()
      grass()
      cloud()
      river()
    

main()

