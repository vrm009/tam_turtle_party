# Turtle Party Project Lesson 
# Instructor Dr. Emily 
# Student Tammie 
# 06-27-24

import turtle 
turtle.color("green")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
# forward helper function
def move(len):
  back(-1 * len)
  
def polygon(num,size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360 / num)
    
# def square(size):
#  for i in range(4):
#    turtle.forward(size)
#    turtle.left(90)
    
for n in range (3,10):
  move(50) # forward
  polygon(n, 100/n)
  back(50)
  turtle.right(360 / 7)
