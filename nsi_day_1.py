from turtle import *
from random import randint 

speed(3)

#  carré rouge 
color('red')
for n in range(1, 5):
    forward(100)
    left(90)

# hexagone 100 pixels de cote 
penup()
goto(-200, 100)
pendown()
color('blue')

for n in range(1, 7):
    forward(100)
    left(60)

# hexagone 150 pixels cote 
penup()
goto(-200, -200)
pendown()
color('yellow')

for n in range(1, 7):
    forward(150)
    left(60)

speed(10)
# les 10 carrés qui s'agrandissent au fur et à mesure 
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

speed(3)
clear()

# TANT QUE JE N'Y SUIS PAS, J'AVANCE !!!

# ----------------------------------------
x_objectif = randint(200, 300)
y_objectif = randint(100, 150)
penup()
goto(x_objectif, y_objectif) 
color('yellow')
dot(25)
goto(0,0)
pendown()
color('black')
# -----------------------------------------
# MON PROGRAMME :

print(x_objectif, y_objectif)



compteur = 0
yes = True 

while xcor() != x_objectif:
    if yes:
        fd(1)
        compteur += 1 
    
if xcor() == x_objectif:
    lt(90)
    yes = False 

while ycor() != y_objectif:
    fd(1)

if ycor() == y_objectif:    
    bgcolor('green')
    
print(compteur)





     





mainloop()