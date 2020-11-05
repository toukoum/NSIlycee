from math import *

# ___________________________________________
# EXERCICE 1 
# ___________________________________________

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
    return resultat                 # si n = 0 la boucle n'est pas effectuée
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

n = 5
print(factorielle(3))       # remarquez que la valeur de n dans la fonction
                            # factorielle n'est pas 5
print(arrangements(3,n))    # l'argument d'une fonction peut être une variable
print(combinaisons(n-1,n))  # l'argument d'une fonction peut être un calcul

# _________________________________________________________________
# EXERCICE 2
# _________________________________________________________________



def volume_sphere(rayon : int) -> int:
    """
        calcul le volume d'une sphère avec en paramètre le rayon 
    """
    volume = 4/3*pi*rayon**3
    return volume

rayon = 0
while volume_sphere(rayon) <= 10000:                   # 1 Litre est égal à 10 000cm3
    rayon += 1
print("Le rayon doit être compris entre : {} et {}.".format(rayon-1, rayon+1))




# _________________________________________________________________
# EXERCICE 3
# _________________________________________________________________


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


def est_premier() -> bool:
    """
        indique si le nombre donné précédement par l'utilisateur est premier ou non et retourne un booléen.
    """
    if len(nbre_diviseur()) == 2:
        return True 
    else:
        return False 

print(nbre_diviseur())
print(est_premier())



from math import *

# ___________________________________________
# EXERCICE 1
# ___________________________________________


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
    return resultat                 # si n = 0 la boucle n'est pas effectuée
                                    # on renvoie donc 1

def arrangements(n_elem, n_tot : int) -> int :
    """nombre d'arrangements possibles de n_elem éléments parmi n_tot éléments
    l'ordre des éléments est important : A,B n'est pas B,A"""
    return factorielle(n_tot) // factorielle (n_tot - n_elem)


def combinaisons(n_elem, n_tot : int) -> int or float:
    """nombre de combinaisons possibles de n_elem éléments parmi n_tot éléments
    l'ordre des éléments n'a pas d'importance : A,B et B,A comptent pour une
    seule combinaison"""

# Le programme principal ne commence qu'ici :
    result = n_tot / (n_elem * (n_tot - n_elem))
    assert type(result) == int
    assert result > 0
    return result

n = 5
print(factorielle(3))       # remarquez que la valeur de n dans la fonction
                            # factorielle n'est pas 5
print(arrangements(3,n))    # l'argument d'une fonction peut être une variable
print(combinaisons(n-1,n))  # l'argument d'une fonction peut être un calcul

# _________________________________________________________________
# EXERCICE 2
# _________________________________________________________________



def volume_sphere(rayon : int) -> int:
    """
        calcul le volume d'une sphère avec en paramètre le rayon
    """
    assert rayon >= 1
    volume = 4/3*pi*rayon**3
    assert type(volume) == int or float
    assert volume > 0
    return volume

rayon = 1
while volume_sphere(rayon) <= 10000:                   # 1 Litre est égal à 10 000cm3
    rayon += 1

print("Le rayon doit être compris entre : {} et {}.".format(rayon-1, rayon+1))




# _________________________________________________________________
# EXERCICE 3
# _________________________________________________________________


def nbre_diviseur() -> int :
    """
        retourne les diviseur du nombre entré par l'utilisateur
    """

    nombre = 0
    while nombre <= 0:                              # verifie que le nombre entré âr l'utilisateur est positif,
        nombre = input("Entrez un nombre :")        # et si c'est bien un nombre et pas un str ou autre
        try :
            nombre = int(nombre)                    # autre manière de assert avec try et exept
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
            assert type(i) == int
            assert i > 0
            factor.append(i)
    return factor


def est_premier() -> bool:
    """
        indique si le nombre donné précédement par l'utilisateur est premier ou non et retourne un booléen.
    """
    return len(nbre_diviseur()) == 2

print(nbre_diviseur())
print(est_premier())

