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
    """
        retourne les diviseur du nombre entré par l'utilisateur
    """

    nombre = 0
    while nombre <= 0:                              # verifie que le nombre entré âr l'utilisateur est positif,
        nombre = input("Entrez un nombre :")        # et si c'est bien un nombre et pas un str ou autre 
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
    # ecris tous les diviseurs de nombre 
    factor = []
    for i in range(1, nombre+1):
        if nombre % i == 0:
            factor.append(i)
    return factor



def est_premier():
    """
        indique si le nombre donné précédement par l'utilisateur est premier ou non.
    """
    if len(nbre_diviseur()) == 2:
        return True 
    else:
        return False 

def est_premier_bis():
    
    compteur = 2
    nbre_diviseur()
    while compteur <= sqrt(nombre):
        if nbre_diviseur() % 2 == 0:
            return ("{} n'est pas un nombre premier ".format(nbre_diviseur))   
        compteur += 1
    return("{} est un nombre premier ".format(nbre_diviseur))
 







n = 5
print(factorielle(3))       # remarquez que la valeur de n dans la fonction
                            # factorielle n'est pas 5
print(arrangements(3,n))    # l'argument d'une fonction peut être une variable
print(combinaisons(n-1,n))  # l'argument d'une fonction peut être un calcul
print(volume_sphere(1))
print(nbre_diviseur())
print(est_premier())
print(est_premier_bis())