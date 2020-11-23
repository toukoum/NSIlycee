# # ____________________________________________
# # EXERCICE 1
# # ____________________________________________


def est_float(tuples : tuple) -> bool:
    """
        fonction qui renvoit True si tous les éléments du tuple sont un float
    """
    for x in range(len(tuples)):
        if type(tuples[x]) != float:
            return False
        return True


a = (12.0, 15.0, 16.5, 13.5, 9.0, 18.0, 11.5, 17.0)
assert(est_float((3,)) == False)
assert(est_float((3.0,)) == True)

print(est_float((a)))

# ____________________________________________
# EXERCICE 2
# ____________________________________________

def verif(tuples : tuple) -> bool:
    """
        fonction qui True si tous les éléments du tuple sont un float
    """
    for x in range(len(tuples)):
        if type(tuples[x]) != float:
            return False
        return True



def moyenne(tuples : tuple) -> float:
    """
        fonction qui fait la moyenne des float donnés en paramètre 
    """
    total = 0
    for x in range(len(tuples)):
        total+=tuples[x]
    return total / len(tuples)


a = (12.0, 15.0, 16.5, 13.5, 9.0, 18.0, 11.5, 17.0)
assert(moyenne((5.0, 15.0)) == 10)
if verif(a):
    print('La moyenne est de : {}'.format(moyenne(a)))	


# ____________________________________________
# EXERCICE 3
# ____________________________________________

def verif(tuples : tuple) -> bool:
    """
        fonction qui True si tous les éléments du tuple sont un float
    """
    for x in range(len(tuples)):
        if type(tuples[x]) != float:
            return False
        return True

def max_min(tuples : tuple) -> tuple:
    """
        fonction qui revoie la valeur max et min d'un tuple  
    """
    min_ = tuples[0]
    max_ = tuples[0]
    for x in range(len(tuples)):
        if tuples[x] < min_ :
            min_ = tuples[x]
        if tuples[x] > max_ :
            max_ = tuples[x]

    return min_, max_
           
           	
a = (12.0, 15.0, 16.5, 13.5, 9.0, 18.0, 11.5, 17.0)
assert (max_min((5.0, 15.0, 10.0)) == 5.0, 15.0)
if verif(a):
    print('Les valeurs minimum et maximum sont : {}'.format(max_min(a)))



# ____________________________________________
# EXERCICE 4
# ____________________________________________
	
def verif(tuples : tuple) -> bool:
    """
        fonction qui True si tous les éléments du tuple sont un float
    """
    for x in range(len(tuples)):
        if type(tuples[x]) != float:
            return False
        return True

def index_max_min(tuples : tuple) -> tuple:
    """
        fonction qui revoit la valeur max et min d'un tuple  
    """
    min_ = tuples[0]
    max_ = tuples[0]
    for x in range(len(tuples)):
        if type(tuples[x]) != float:
            return False
      
        if tuples[x] < min_ :
            min_ = tuples[x]
        if tuples[x] > max_ :
            max_ = tuples[x]

    return tuples.index(min_), tuples.index(max_)
           
           	
a = (12.0, 15.0, 16.5, 13.5, 9.0, 18.0, 11.5, 17.0)
assert (index_max_min((5.0, 15.0, 10.0)) == 0, 2)
if verif(a):
    print("L'index des valeurs minimum et maximum sont : {}".format(index_max_min(a)))

# ____________________________________________
# EXERCICE 5
# ____________________________________________

def verif(tuples : tuple) -> bool:
    """
        fonction qui True si tous les éléments du tuple sont un float
    """
    for x in range(len(tuples)):
        if type(tuples[x]) != float:
            return False
        return True

def moyenne(tuples : tuple) -> float:
    """
        fonction qui fait la moyenne des float donnés en paramètre 
    """
    total = 0
    for x in range(len(tuples)):
        total+=tuples[x]
    return total / len(tuples)

def moyenne_inf(tuples : tuple) -> tuple:
    """
        fonction qui revoit le nombre de valeurs superieur et inferieur a la moyenne du tuple  
    """
    total = 0
    compteur_inf = 0
    compteur_sup = 0

    for x in range(len(tuples)):   
        if tuples[x] < moyenne(tuples):
            compteur_inf += 1
        else:
            compteur_sup += 1
    return compteur_inf, compteur_sup
           	
a = (12.0, 15.0, 16.5, 13.5, 9.0, 18.0, 11.5, 17.0)
assert (moyenne_inf((5.0, 15.0, 10.0)) == 1, 2)
if verif(a):
    print("Les valeurs en dessous de la moyenne et égales ou superieurs sont : {}".format(moyenne_inf(a)))



# ____________________________________________
# EXERCICE 6
# ____________________________________________



# def date(x, y, z: tuple) -> str:
#     """
#         fonction qui revoit la date d'un tuple écrit en toute lettre
#     """
    
           	
# a = (4, 11, 1)
# assert ()
# print("La date est : {}".format(date(a)))