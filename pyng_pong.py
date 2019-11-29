# -*- coding: utf-8 -*-
"""
Created on Thur Nov 28 16:25:35 2019

@author: pushparajkarthick_d
"""

import turtle
import keyboard
from tkinter import messagebox as mb
import winsound as ws 

yvelo = 3
xvelo = 2
counter = 0
count = 0
distance = 15
paddx = 2.5

# Pen for score
pen = turtle.Turtle()
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 0)

# Main Window
win = turtle.Screen()
win.title("Pyng_Pong Game")
win.bgcolor("cyan")
win.setup(width=600,height=600)
win.tracer(0)

#Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.pu()
ball.shapesize(1, 1)
ball.goto(0, 0)

# Paddles, Controlled by human
padh1 = turtle.Turtle()
padh1.shape("square")
padh1.color("black")
padh1.shapesize(0.3,0.2)
padh1.pu()
padh1.goto(10,-215)

padh2 = turtle.Turtle()
padh2.shape("square")
padh2.color("black")
padh2.shapesize(0.3,0.2)
padh2.pu()
padh2.goto(6,-215)

padh3 = turtle.Turtle()
padh3.shape("square")
padh3.color("black")
padh3.shapesize(0.3,0.2)
padh3.pu()
padh3.goto(2,-215)

padh4 = turtle.Turtle()
padh4.shape("square")
padh4.color("black")
padh4.shapesize(0.3,0.2)
padh4.pu()
padh4.goto(-2,-215)

padh5 = turtle.Turtle()
padh5.shape("square")
padh5.color("black")
padh5.shapesize(0.3,0.2)
padh5.pu()
padh5.goto(-6,-215)

padh6 = turtle.Turtle()
padh6.shape("square")
padh6.color("black")
padh6.shapesize(0.3,0.2)
padh6.pu()
padh6.goto(-10,-215)

padh7 = turtle.Turtle()
padh7.shape("square")
padh7.color("black")
padh7.shapesize(0.3,0.2)
padh7.pu()
padh7.goto(-14,-215)

padh8 = turtle.Turtle()
padh8.shape("square")
padh8.color("black")
padh8.shapesize(0.3,0.2)
padh8.pu()
padh8.goto(-18,-215)

padh9 = turtle.Turtle()
padh9.shape("square")
padh9.color("black")
padh9.shapesize(0.3,0.2)
padh9.pu()
padh9.goto(-22,-215)

padc = turtle.Turtle()
padc.shape("square")
padc.color("black")
padc.shapesize(0.30,1.8)
padc.pu()
padc.goto(0,210)

#Walls
wall1 = turtle.Turtle()
wall1.shape("square")
wall1.color("red")
wall1.shapesize(0.01,23)
wall1.pu()
wall1.goto(0,215)

wall2 = turtle.Turtle()
wall2.shape("square")
wall2.color("red")
wall2.shapesize(0.01,23)
wall2.pu()
wall2.goto(0,-220)

wall3 = turtle.Turtle()
wall3.shape("square")
wall3.color("black")
wall3.shapesize(20,1)
wall3.pu()
wall3.goto(227,0)

wall4 = turtle.Turtle()
wall4.shape("square")
wall4.color("black")
wall4.shapesize(20,1)
wall4.pu()
wall4.goto(-227,0)

def move():
    xco = ball.xcor()
    yco = ball.ycor()
    ball.sety(yco+yvelo)
    ball.setx(xco+xvelo)

def go_right():
    padh1x = padh1.xcor()
    padh2x = padh2.xcor()
    padh3x = padh3.xcor()
    padh4x = padh4.xcor()
    padh5x = padh5.xcor()
    padh6x = padh6.xcor()
    padh7x = padh7.xcor()
    padh8x = padh8.xcor()
    padh9x = padh9.xcor()

    if padh1x >= 205:
        pass
    else:
        padh1.setx(padh1x+paddx)
        padh2.setx(padh2x+paddx)
        padh3.setx(padh3x+paddx)
        padh4.setx(padh4x+paddx)
        padh5.setx(padh5x+paddx)
        padh6.setx(padh6x+paddx)
        padh7.setx(padh7x+paddx)
        padh8.setx(padh8x+paddx)
        padh9.setx(padh9x+paddx)

def go_left():
    padh1x = padh1.xcor()
    padh2x = padh2.xcor()
    padh3x = padh3.xcor()
    padh4x = padh4.xcor()
    padh5x = padh5.xcor()
    padh6x = padh6.xcor()
    padh7x = padh7.xcor()
    padh8x = padh8.xcor()
    padh9x = padh9.xcor()

    if padh9x < -205:
        pass

    else:
        padh1.setx(padh1x-paddx)
        padh2.setx(padh2x-paddx)
        padh3.setx(padh3x-paddx)
        padh4.setx(padh4x-paddx)
        padh5.setx(padh5x-paddx)
        padh6.setx(padh6x-paddx)
        padh7.setx(padh7x-paddx)
        padh8.setx(padh8x-paddx)
        padh9.setx(padh9x-paddx)

def cheat():
    if ball.ycor() < 0:
        padh1.setx(ball.xcor())
        padh2.setx(ball.xcor()+12)
        padh3.setx(ball.xcor()+8)
        padh4.setx(ball.xcor()+4)
        padh5.setx(ball.xcor())
        padh6.setx(ball.xcor()-4)
        padh7.setx(ball.xcor()-8)
        padh8.setx(ball.xcor()-12)
        padh9.setx(ball.xcor()-16)

def gameover():
    global counter
    global xvelo
    global yvelo
    global count
    mb.showinfo("GO","GAME OVER \n Score: %s" %(int(counter)))
    pen.clear()
    pen.write("Press 'R' to replay\n  'E' to exit", align="center", font=("Courier", 25, "normal"))
    while True:
        if keyboard.is_pressed("r"):
            counter = 0
            count = 0
            yvelo = 3
            xvelo = 2
            ball.goto(0,0)
            padh1.goto(10,-215)
            padh2.goto(6,-215)
            padh3.goto(2,-215)
            padh4.goto(-2,-215)
            padh5.goto(-6,-215)
            padh6.goto(-10,-215)
            padh7.goto(-14,-215)
            padh8.goto(-18,-215)
            padh9.goto(-22,-215)
            win.update()
            break
        if keyboard.is_pressed("e"):
            exit()
        else:
            pass

print("PLAY NOW")
win.update()
pen.write("Press arrow key to start", align="center", font=("Courier", 22, "normal"))

while True:
    count = count+1
    win.update()
    if ball.ycor() >= 200:
        yvelo = -yvelo

    if ball.xcor() >= 205 or ball.xcor() <= -205:
        xvelo = -xvelo

    if keyboard.is_pressed("right"):
        go_right()

    if keyboard.is_pressed("left"):
        go_left()

    if ball.ycor() < -207:
        gameover()

    if ball.ycor() >= 00:
        padc.setx(ball.xcor())

    if keyboard.is_pressed("c"):
        cheat()

    if count % 700 == 0 and count > 0:
        if xvelo >= 0:
            xvelo += 0.1

        if xvelo < 0:
            xvelo += -0.1

        if yvelo >= 0:
            yvelo += 0.1

        if yvelo <0:
            yvelo += -0.1

        print(xvelo, yvelo)

    if (padh1.distance(ball) < distance) or (padh2.distance(ball) < distance) or (padh3.distance(ball) < distance) or (padh4.distance(ball) < distance) or (padh5.distance(ball) < distance) or (padh6.distance(ball) < distance) or (padh7.distance(ball) < distance) or (padh8.distance(ball) < distance) or (padh9.distance(ball) < distance):
        if ball.ycor() < -205:
            ball.sety(-207.1)
        else:
            yvelo = -yvelo
            counter+=10
    pen.clear()
    pen.write("Score: %s" %(int(counter)), align="center", font=("Courier", 40, "normal"))
    move()


