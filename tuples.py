# ____________________________________________
# EXERCICE 1
# ____________________________________________


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
           
           	
a = (9.0, 15.0, 16.5, 13.5, 12.0, 18.0, 11.5, 17.0)
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
        fonction qui revoit le nombre de valeurs superieur ou égale et inferieur à la moyenne du tuple  
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



____________________________________________
EXERCICE 6
____________________________________________



def date(x, y, z: tuple) -> str:
    """
        fonction qui revoit le jour de la semaine d'un tuple écrit en toute lettre
    """
    assert(type(x)== int)
    assert(type(y)== int)
    assert(type(z)== int)
    assert(x>=1) and (x<= 31)
    assert(y>=1) and (y<=12)
    assert(z>=1) and (z<=7)
    
    tuples_mois = (
        'janvier', 'février', 'mars', 'avril', 
        'mai', 'juin', 'juillet', 'aout', 
        'septembre', 'octobre', 'novembre',
        'décembre')

    tuples_jour = (
        'lundi', 'mardi', 'mercredi', 'jeudi', 
        'vendredi', 'samedi', 'dimanche')



    return "{} {} {}".format(tuples_jour[z-1], x, tuples_mois[y-1])
           	

assert(date(4, 11, 1) == "lundi 4 novembre")
assert(date(10, 1, 5) == "vendredi 10 janvier")
print("La date est : {}".format(date(4, 11, 3)))        # appelle de la fonction à
                                                        # modifier 




# ____________________________________________
# EXERCICE 7 et 8
# ____________________________________________


def nombre_correct_jour()-> int:
    """
        Fonction qui demande le jour et verifie si c'est bien un int 
    """
    valid = True
    
    while valid:
        saisie = input("Entrez le jour sous forme d'entier : ")
        try:
            saisie = int(saisie)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            continue
        if saisie < 0:
            print("Ce nombre est négatif")
            continue
        if saisie > 31:
            print("Ce nombre est supérieur à 31")
            continue
        valid = False

        return saisie

def nombre_correct_mois() -> int:
    """
        Fonction qui demande le mois et verifie si c'est bien un int 
    """
    valid = True
    
    while valid:   
        saisie_mois = input("Entrez le mois sous forme d'entier : ")
        try:
            saisie_mois = int(saisie_mois)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            continue
        if saisie_mois < 0:
            print("Ce nombre est négatif")
            continue
        if saisie_mois > 12:
            print("Il n'y a que 12 mois en un an ;)")
            continue
        valid = False

    return saisie_mois


def nombre_correct_année() -> int:
    """
        Fonction qui demande l'année et verifie si c'est bien un int 
    """
    valid = True
    
    while valid:   
        saisie_année = input("Entrez l'année sous forme d'entier (entre 1900 et 2100): ")
        try:
            saisie_année = int(saisie_année)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            continue
        if saisie_année < 1900:
            print("Ce nombre est en dessous de 1900")
            continue
        if saisie_année > 2100:
            print("Ce nombre est supérieur à 2100")
            continue
        valid = False

    return saisie_année


def formule_and_affichage() -> tuples:
    """
        Alors j'ai essayé de simplifié mon code au max, je sais que c'est pas encore parfait et qu'on pourrait amélioré
        encore le code et j'espere que vous aller pas trop galérer à le comprendre 
        A l'aide d'une formule, on détermine un total qui corespond au jour de la semaine (1 -> lundi, 2 -> mardi...)
        La formule pour les années au dessus de 2000: (jour + code_mois + année[2:] + année[2:]//4 - 2)%7
        La formule pour les années en dessous de 2000: (jour + code_mois + année[2:] + année[2:]//4 - 1)%7
        Après c'est que de l'affichage ;)
        Je sais que ce n'est pas exactement ce que vous atendiez mais je trouvait l'exercice intéressant du coup 
        je me suis fait plaisir !
        PS: j'ai pas fait de assert parce que je fait try exep, j'aime bien
    """

    code_mois = (1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 4)
    
    tuples_jour = ('lundi', 'mardi', 
                   'mercredi', 'jeudi', 
                   'vendredi', 'samedi', 
                   'dimanche')
    
    tuples_mois = (
        'janvier', 'février', 'mars', 'avril', 
        'mai', 'juin', 'juillet', 'aout', 
        'septembre', 'octobre', 'novembre',
        'décembre')

    saisie_jour = nombre_correct_jour()
    saisie_mois = nombre_correct_mois()
    saisie_année = nombre_correct_année()

    
    

    if saisie_année < 2000:
        an = str(saisie_année)                  # la j'ai séché pour prendre les deux dernières valeurs  
        an = an[2:]                             # de l'année, par exemple 2015 -> 15
        an_2 = int(an)                          # du coup je le transforme en str pour faire an = an[2:]
        an_2 %=7
        an_bis = str(saisie_année)
        an_bis = an_bis[2:]
        an_bis_2 = int(an_bis)
        an_bis_2 //= 4
        total = (saisie_jour + code_mois[saisie_mois-1] + an_2 + an_bis_2 - 1)%7
        print(total)
    elif saisie_année >= 2000:
        an = str(saisie_année)                #idem que pour les valeurs en dessous de 2000
        an = an[2:]
        an_2 = int(an)
        an_2 %=7
        an_bis = str(saisie_année)
        an_bis = an_bis[2:]
        an_bis_2 = int(an_bis)
        an_bis_2 //= 4
        total = (saisie_jour + code_mois[saisie_mois-1] + an_2 + an_bis_2 - 2)%7
    
    return ('La date complete du {}/{}/{} est : '.format(saisie_jour, saisie_mois, saisie_année),
    tuples_jour[total-1], ' ', saisie_jour, ' ', tuples_mois[saisie_mois - 1], ' ', saisie_année)
    

for x in formule_and_affichage():           #la fonction formule retourne un tuple donc on affiche 
    print(x, end = '')                      # pas directement le retour de la fonction

print('\n')
