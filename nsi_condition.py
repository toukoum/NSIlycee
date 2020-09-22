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


from tkinter import *

fenetre=Tk()

def clavier(event):
    global coords

    touche = event.keysym

    if touche =="Up":
        coords = (coords[0], coords[1]-10)
    elif touche =="Down":
        coords = (coords[0], coords[1]+10)
    elif touche =="Right":
        coords = (coords[0]+10, coords[1])
    elif touche =="Left":
        coords = (coords[0]-10, coords[1]-10)
    
    canvas.coords(rectangle_jaune, coords[0], coords[1], coords[0]+25, coords[1]+25)

    canvas.config(bg = 'green') 
    
    if len(canvas.find_overlapping(canvas.coords(rectangle_bleu)[0], canvas.coords(rectangle_bleu)[1], canvas.coords(rectangle_bleu)[2], canvas.coords(rectangle_bleu)[3]))>1: 
        canvas.configure(bg = 'red')

 
canvas = Canvas(fenetre, width=500, height=500, bg='ivory')
coords=(0, 0)

canvas.config(bg = 'green') 

rectangle_jaune = canvas.create_rectangle(0, 0, 25, 25, fill="cyan")
rectangle_bleu = canvas.create_rectangle(250, 250, 325, 325, fill="blue") 

canvas.focus_set()
canvas.bind("<Key>", clavier)
canvas.pack()

fenetre.mainloop()
