from turtle import *

shape('turtle')

color('red')

for n in range(1, 5):
    forward(100)
    left(90)

penup()
goto(-200, 100)
pendown()

color('blue')

for n in range(1, 7):
    forward(100)
    left(60)

penup()
goto(-200, -200)
pendown()

color('yellow')

for n in range(1, 7):
    forward(150)
    left(60)

penup()
goto(110, 100)
pendown()

color('green')

d=100

for a in range(1, 11):
    for b in range(1, 5):
        forward(d)
        left(90)
    d+=10

if True:
    print('bonjour')

turtle.exitonclick()
mainloop()