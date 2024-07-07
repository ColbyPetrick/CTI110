# Colby Petrick
# July 7th 2024
# Utilizing Turtle to sign
# P4LAB1b
import turtle

t = turtle.Turtle()
close = turtle.Screen()

# No loops used - as per given instructions not requiring their usage in segment b. If I was mistaken let me know and I can get a loop set up
t.color('blue')
side_length = 100;
t.pensize(4)
sl = side_length
# Intial C
t.right(90)
t.forward(sl)
t.left(180)
t.forward(sl)
t.right(90)
t.forward(sl)
t.left(180)
t.forward(sl)
t.left(90)
t.forward(sl)
t.left(90)
t.forward(sl)

# Initial P
t.penup()
t.forward(50)
t.left(90)
t.forward(100)
t.pendown()
t.right(90)
t.forward(sl)
t.left(180)
t.forward(sl)
t.left(90)
t.forward(50)
t.left(90)
t.forward(sl)
t.left(90)
t.forward(50)
t.right(180)
t.forward(50)
t.right(90)
t.forward(sl)
t.left(90)
t.forward(50)

# Notes: Whilst I would rather the P be more curved - I have determined to handle with just a box based P instead

close.mainloop()
    