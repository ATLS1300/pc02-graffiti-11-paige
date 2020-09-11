#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

up()
home()

goto(17,75)
color('red')
fillcolor('red')
begin_fill()
down()
width(1)
circle(15)
end_fill()

up()
goto(20,150)
color('green')
down()
begin_fill()
forward(45)
right(90)
forward(12)
right(90)
forward(45)
right(90)
forward(12)
end_fill()
up()

goto(-1,138)
down()
begin_fill()
backward(12)
right(90)
backward(45)
left(90)
forward(12)
right(90)
forward(45)
end_fill()
up()

goto(-1,10)
color(250,200,0)
down()
width(7)
forward(35)
right(110)
forward(52)
right(140)
forward(52)
up()

home()
goto(108,-87)
right(15)
color(255,153,51)
width(3)
down()
forward(267)


