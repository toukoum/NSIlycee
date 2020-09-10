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
from turtle import *
from random import *

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
    if compteur >= 250:
        color('red')

if xcor() == x_objectif:
    lt(90)
    yes = False

yep = True

while ycor() != y_objectif:
    if yep:
        fd(1)
        compteur +=1
    if compteur >= 250:
        color('red')

if ycor() == y_objectif:
    bgcolor('green')
    yep = False



print(compteur)

mainloop()


# -------------------------------------------------
# EXERCICE 4  

#1 les 10 carrés qui diminue au fur et à mesure 
clear()

speed(10)
penup()
goto(0,0)
pendown()
color('cyan')

d=200

for a in range(1, 11):
    for b in range(1, 5):
        forward(d)
        left(90)
    d-=10

# 2 les 10 carrés qui diminue mais avec le meme centre 

speed(3)
clear()
goto(0,0)

d=200

for a in range(1, 11):
    for b in range(1, 5):
        forward(d)
        left(90)
    lt(45)
    up()
    fd(7)
    down()
    rt(45)
    d-=10

#3 quadrillage 2x2 cote de 100
#4 ancien logo de microsoft 

speed(3)
clear()
up()
goto(0,0)
down()
color('white')
width(3)

# définissons ce qu'est un carré
def carre():
  for cote in range(4):
    fd(100)
    lt(90)

fillcolor('green')
begin_fill()
carre()
end_fill()

fillcolor('blue')
begin_fill()
rt(180)
carre()
end_fill()

fillcolor('yellow')
begin_fill()
lt(90)
carre()
end_fill()

fillcolor('red')
begin_fill()
rt(180)
carre()
end_fill()





mainloop()