from math import *


def factorielle(n : int) -> int :
    """fonction factorielle
    factorielle(n) = n! = 1 * 2 * 3 *...* n et 0! = 1
    cela correspnd au nombre de permutations qu'on peut faire avec n �l�ments"""
    # la chaine ci-dessus n'est pas obligatoire, mais conseill�e :
    # on l'appelle DOCSTRING : si vous faites un help sur la fonction
    # la docstring est affich�e
    resultat = 1
    for i in range(n) :
        resultat = resultat*(i+1)   # i+1 prend les valeurs 1,2,3,...n
    return resultat                 # si n = 0 la boucle n'est pas effectu�e
                                    # on renvoie donc 1

def arrangements(n_elem, n_tot : int) -> int :
    """nombre d'arrangements possibles de n_elem éléments parmi n_tot éléments
    l'ordre des éléments est important : A,B n'est pas B,A"""
    return factorielle(n_tot) // factorielle (n_tot - n_elem)


def combinaisons(n_elem, n_tot : int) -> int :
    """nombre de combinaisons possibles de n_elem éléments parmi n_tot éléments
    l'ordre des éléments n'a pas d'importance : A,B et B,A comptent pour une
    seule combinaison"""

# Le programme principal ne commence qu'ici :
    result = n_tot / (n_elem * (n_tot - n_elem))
    return result


def volume_sphere(rayon : int) -> int :
    volume = 0
    while volume <= 10000:
        rayon += 1
        volume = 4/3*pi*rayon**3
    return rayon, volume



def nbre_diviseur() -> int :
    nombre = 0
    while nombre <= 0:
        nombre = input("Entrez un nombre :")
        try :
            nombre = int(nombre)
        except ValueError:
            print("Ce n'est pas un nombre !")
            nombre = 0
            continue
        if nombre < 0:
            print('Ce nombre est négatif !')
        if nombre == 0:
            print('Ce nombre est égal à zéro !')
    for i in range(1, nombre+1):
        if nombre % i == 0:
            print(i)
    for i in range(1, nombre+1):

        if nombre % i == 1:
            if nombre == i:
                if nombre % i == 1:
                    print("{}est un nombre premier ".format(nombre))





n = 5
print(factorielle(3))       # remarquez que la valeur de n dans la fonction
                            # factorielle n'est pas 5
print(arrangements(3,n))    # l'argument d'une fonction peut être une variable
print(combinaisons(n-1,n))  # l'argument d'une fonction peut être un calcul
print(volume_sphere(1))
print(nbre_diviseur())