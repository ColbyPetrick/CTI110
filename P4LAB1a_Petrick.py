# Colby Petrick
# July 7th 2024
# Utilizing Turtle & Loops to create shapes
# P4LAB1a
import turtle

# Utilizing a given example to simplify certain aspects
t = turtle.Turtle()
close = turtle.Screen()

# Notes: This is a first draft attempt - utilizing a while loop as the base
x = 0
y = 0
t.pensize(3)
while x < 4:
    side_length = 50;
    t.forward(side_length)
    t.left(90)
    x += 1
    if x >= 4: # Utilizing if statement within while loop
        t.pensize(0) # Was attempting to make it invisible - however this was closet I could get
        t.forward(100)
        t.pensize(3)
        t.forward(100)
        t.left(120)
        t.forward(100)
        t.left(120)
        t.forward(100)
        # Tried using smaller numbers however I was unable to get it to work w/o using the turtle4_triangle example
close.mainloop()