# Shalay Pridgen
#CTI 110
# 7 Nov 2022
# LAB: Shapes ( Square and Triangle)

import turtle
box = turtle.Screen()
x = turtle.Turtle()
c = 1

x.pensize(5)
while c <= 4:
    x.pencolor("red")
    x.forward(60)
    x.left(90)
    c += 1

x.penup()
x.forward(90)
x.pendown()

f = 1
while f <= 3:
    x.pencolor("blue")
    x.forward(130)
    x.left(120)
    f += 1
    
box.mainloop()
