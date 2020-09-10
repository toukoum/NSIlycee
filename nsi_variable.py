from lycee import demande
from turtle import *


#1 degrés en Kelvin
x = demande('Conversion de degrés en kelvin :')
print('{} degrés représente {} kelvin.'.format(x, x+240))

#2 temps écoulé

x = int(input("Entrez les heures :"))
y = int(input("Entrez les minutes :"))
z = int(input("Entrez les secondes :"))

print(x,'h', y,'min et', z,'s corespondent à :')
##en secondes
a = x*3600 + y*60 + z
print(a, 'secondes ; le type de cette variable est :', type(a))

##en minutes
b = x*60 + y + z/60
print(b, 'minutes ; le type de cette variable est :', type(b))

##en heures
c = x + y/60 + z/3600
print(c, 'heures ; le type de cette variable est :', type(c))

##en jours
d = x/24 + y/1440 + z/86400
print(d, 'jours ; le type de cette variable est :', type(d))

#3 temps en seconde to temps en heure, minute et seconde

x = int(input("Entrez les secondes :"))


heure = x // 3600
minute = x -(3600*heure)
minute_2 = minute // 60
secondes = x - 3600*heure - 60*minute_2
print("{} secondes représentent : {} heures, {} minutes, et {} secondes".format(x, heure, minute_2, secondes))

#4 voici un programme

x = demande('Entrez la valeur de la variable x :')
y = demande('Entrez la valeur de la variable y :')

print('x =', x, 'y =', y)

x = y
y = x

print("Après échange : x =", x, "et y =", y)

#5 cercle

for angle in range(360):
    fd(1.5)
    lt(1)                               #quand on a tourné 360 fois de 1° on a fait 1 tour

for angle in range(360):
    for angle in range(360):
        lt(1.5)

    fd(1.5)
    lt(10)                               #quand on a tourné 360 fois de 1° on a fait 1 tour

mainloop()