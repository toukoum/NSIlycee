from lycee import demande

#1 comparaison de programmes
#le programme 1 dit "merci pour votre participation que si le nombre n'est pas egal à 7
# alors que le second programme dit "merci pour votre participation" dans tous les cas.


#2 rangé du plus petit au plus grand + cas d'égalité

nombre_1 = demande('Entrez le 1er nombre')
nombre_2 = demande('Entrez le 2eme nombre')
nombre_3 = demande('Entrez le 3eme nombre')



if nombre_1 <= nombre_2 <= nombre_3 :
    if nombre_1 == nombre_2 :
        print('{} = {} <= {}'.format(nombre_1,nombre_2,nombre_3))
    elif nombre_2 == nombre_3 :
        print('{} <= {} = {}'.format(nombre_1,nombre_2,nombre_3))
    else :
        print('{} <= {} <= {}'.format(nombre_1,nombre_2,nombre_3))



elif nombre_1 <= nombre_3 <= nombre_2 :
    if nombre_1 == nombre_3 :
        print('{} = {} <= {}'.format(nombre_1,nombre_3,nombre_2))
    elif nombre_3 == nombre_2 :
        print('{} <= {} = {}'.format(nombre_1,nombre_3,nombre_2))
    else :
        print('{} <= {} <= {}'.format(nombre_1,nombre_3,nombre_2))



elif nombre_2 <= nombre_3 <= nombre_1 :
    if nombre_2 == nombre_3 :
        print('{} = {} <= {}'.format(nombre_2,nombre_3,nombre_1))
    elif nombre_3 == nombre_1 :
         print('{} <= {} = {}'.format(nombre_2,nombre_3,nombre_1))
    else :
         print('{} <= {} <= {}'.format(nombre_2,nombre_3,nombre_1))


elif nombre_2 <= nombre_1 <= nombre_3 :
    if nombre_2 == nombre_1 :
        print('{} = {} <= {}'.format(nombre_2,nombre_1,nombre_3))
    elif nombre_1 == nombre_3 :
        print('{} <= {} = {}'.format(nombre_2,nombre_1,nombre_3))
    else :
        print('{} <= {} <= {}'.format(nombre_2,nombre_1,nombre_3))


elif nombre_3 <= nombre_1 <= nombre_2 :
    if nombre_3 == nombre_1 :
        print('{} = {} <= {}'.format(nombre_3,nombre_1,nombre_2))
    elif nombre_1 == nombre_2 :
        print('{} <= {} = {}'.format(nombre_3,nombre_1,nombre_2))
    else :
        print('{} <= {} <= {}'.format(nombre_3,nombre_1,nombre_2))


elif nombre_3 <= nombre_2 <= nombre_1 :
    if nombre_3 == nombre_2 :
         print('{} = {} <= {}'.format(nombre_3,nombre_2,nombre_1))
    elif nombre_2 <= nombre_1 :
         print('{} <= {} = {}'.format(nombre_3,nombre_2,nombre_1))
    else :
        print('{} <= {} <= {}'.format(nombre_3,nombre_2,nombre_1))
else :
    print('{} = {} = {}'.format(nombre_1, nombre_2, nombre_3))



#2 BIS (version avec liste ;)

nombre_1 = int(input('Entrez le premier nombre :'))
nombre_2 = int(input('Entrez le premier nombre :'))
nombre_3 = int(input('Entrez le premier nombre :'))

liste=[]
liste.append(nombre_1)
liste.append(nombre_2)
liste.append(nombre_3)

liste.sort()

print(liste)

#3 amelioration du programmme précédent

nombre_1 = int(input('Entrez le premier nombre :'))
nombre_2 = int(input('Entrez le premier nombre :'))
nombre_3 = int(input('Entrez le premier nombre :'))

liste=[]
liste.append(nombre_1)
liste.append(nombre_2)
liste.append(nombre_3)

liste.sort()
liste.insert(1, '<=')
liste.insert(3, '<=')


print(str(liste))



#4 Calcul pour savoir si une année est bissextile

annee = int(input("Saisissez une année : "))

bissextile = False

if annee % 400 == 0: # Si l'année est divisible par 400
    bissextile = True
elif annee % 100 == 0: # Si l'année est divisible par 100
    bissextile = False
elif annee % 4 == 0: # Si l'années est divisible par 4
    bissextile = True

if bissextile:
    print("L'année", annee, "est bissextile")
else:
    print("L'année", annee, "n'est pas bissextile")




#5 Collisions si superposition ou si se touche

collision = False

def collision(x1, y1, L1, h1, L2, h2, x5, y5):
    x2 = x1
    y2 = y1+h1

    x3 = x1+L1
    y3 = y1+h1

    x4 = x1+L1
    y4 = y1

collision(2, 3, 2, 3, 4, 5, 8, 9)