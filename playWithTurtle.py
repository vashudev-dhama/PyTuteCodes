#turtle is a file in py std lib which contain a class Turtle
import turtle
import time

def draw_flower(some_turtle):
    for i in range(0,2):
        #move turtle forward by 100
        some_turtle.forward(100)
        #turn turtle at an angle 40 at right
        some_turtle.right(40)
        some_turtle.forward(100)
        some_turtle.right(140)

def draw_art():
    #get a screen to draw on
    window = turtle.Screen()
    #put a bgcolor to the screen
    window.bgcolor("black")

    #Draws a square:
    #create a instance of class Turtle in memory(via __init__ funtion of Turtle class)
    brad = turtle.Turtle()
    #setup the shape of turtle
    brad.shape("turtle")
    #setup the color of turtle
    brad.color("yellow")
    #setup the speed for turtle movement
    brad.speed(10)
    
    #time.sleep(10)
    for n in range(0,36):
        #calling draw_flower() function
        draw_flower(brad)
        #change the turtle angel by 10 degree
        brad.right(10)

    brad.right(90)
    brad.forward(300)

    #exit the window on click
    window.exitonclick()

draw_art() 