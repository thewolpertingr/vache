from datetime import date # Pour le traitement des dates

# La liste des types d'évènements contenus dans evenements.txt
types_evenements = ['Danse', 'Musique', 'Théâtre']


def obtenir_evenements():
    '''
    Cette fonction va lire le document evenements.txt et en extraire la liste des évènements dans un format
    plus facile à manipuler. Cette fonction a donc 3 parties importantes :

    1) Lire le fichier evenements.txt, où chaque évènement est séparé par un '\n'

    2) Regrouper chaque évènement en une liste où la première entrée est le type de l'évènement, la deuxième est
    son nom, la troisième la date de début de l'évènement et la quatrième la date de fin. Toutes ces informations
    sont présentes, dans cet ordre, sur chacune des lignes représentant un évènement. Elles sont séparées par un '/'.

    3) Traduire les dates du format AAAA-MM-JJ à un nombre entier représentant la position du jour dans l'année 2018.

    ***Pour les parties 1) et 2), vous avez vu en classe une fonction qui vous permet de retourner une liste de
    tous les éléments séparés par un caractère donné dans un string, pensez à y faire appel !***

    ***Pour la partie 3), implémentez d'abord la fonction obtenir_date() et appelez la simplement.***

    Returns:
        La liste des évènements formatés.

    Example:
        Si le fichier evenements.txt était :

        Danse/Samedi de danser.../2018-07-21/2018-07-21
        Musique/Peter Gunn : spécial rétro francophone/2018-07-22/2018-07-24
        Musique/Electric Power Trio/2018-07-31/2018-07-31
        Théâtre/Hamlet/2018-07-31/2018-07-31

        La liste retournée devrait être :

        evenements = [['Danse', 'Samedi de danser...', 202, 202],
                      ['Musique', 'Peter Gunn : spécial rétro francophone', 203, 205],
                      ['Musique', 'Eletric Power Trio', 212, 212],
                      ['Théâtre', 'Hamlet', 212, 212]]
    '''
    # TODO: Programmez cette fonction en retirant l'instruction pass (qui ne fait rien) et en y
    # TODO: ajoutant votre code.
    pass


def creer_dictio_avec_evenements(evenements):
    '''
    Cette fonction va regrouper la liste d'évènements formatés par obtenir_evenements() dans un dictionnaire et
    selon le type de chacun des évènements. Tous les types d'évènements sont recueillis dans la liste de string
    types_evenements définie en haut de ce document.

    Votre travail consiste donc à créer un dictionnaire où les clés seront les types d'évènements et les valeurs
    associées seront une liste d'évènements du type correspondant.

    Args:
        evenements: la liste de tous les évènements recueillis par obtenir_evenements()

    Returns:
        Le dictionnaire des évènements filtrés par type d'évènement

    Example:
        Si la liste evenements était :

        evenements = [['Danse', 'Samedi de danser...', 202, 202],
                      ['Musique', 'Peter Gunn : spécial rétro francophone', 203, 205],
                      ['Musique', 'Eletric Power Trio', 212, 212],
                      ['Théâtre', 'Hamlet', 212, 212]]

        Le dictionnaire retourné devrait être :

        dictionnaire['Danse'] = [['Danse', 'Samedi de danser...', 202, 202]]
        dictionnaire['Musique'] = [['Musique', 'Peter Gunn : spécial rétro francophone', 203, 205],
                                   ['Musique', 'Eletric Power Trio', 212, 212]]
        dictionnaire['Théâtre'] = [['Théâtre', 'Hamlet', 212, 212]]
    '''
    # TODO: Programmez cette fonction en retirant l'instruction pass (qui ne fait rien) et en y
    # TODO: ajoutant votre code.
    pass

def creer_dictio():
    '''
    ***Cette fonction est déjà faite pour vous.***

    Une fois que obtenir_evenements() et creer_dictio_avec_evenements()
    seront implémentés correctement, un appel à creer_dictio() vous permettra d'obtenir le dictionnaire des
    évènements formatés et où les évènements sont filtrés par leur type.

    Returns:
        Le dictionnaire des évènements formatés filtrés selon leur type
    '''
    evenements = obtenir_evenements()

    return creer_dictio_avec_evenements(evenements)


def obtenir_date(date):
    '''
    Cette fonction va traduire la date en format AAAA-MM-JJ contenue dans evenements.txt à un nombre entier
    représentant la position du jour dans l'année 2018. Vous avez donc deux choses à faire dans cette fonction :

    1) Extraire le mois et le jour de la date au format AAAA-MM-JJ. Rappelez-vous que la date en entrée est
    simplement une chaîne de caractères, où l'année, le mois et le jour sont séparés par un '-'.

    2) Faire appel à la fonction obtenir_jour_annee(), qui est déjà implémentée pour vous, pour obtenir le nombre
    entier correspondant à la date en entrée. *

    ***Prenez note que les paramètres mois et jour qui sont passés en entrée à obtenir_jour_annee() sont des ENTIERS,
    pas des string. Vous devez donc faire la conversion en entier avant de faire appel à la fonction.***

    Args:
        date: une string correspondant à une date au format AAAA-MM-JJ que l'on souhaite convertir

    Returns:
         un entier représentant la position de la date en entrée dans l'année 2018.
         Par exemple, on doit retourner 1 pour le 1er janvier et 365 pour les 31 décembre.
    '''
    # TODO: Programmez cette fonction en retirant l'instruction pass (qui ne fait rien) et en y
    # TODO: ajoutant votre code.
    pass


def obtenir_jour_annee(mois, jour):
    '''
    ***Cette fonction est déjà faite pour vous.***

    Cette fonction fait appel à la librairie date de Python, permettant de faire diverses opérations sur des
    dates calendrier comme connaître la différence entre deux dates dans notre cas.

    Args:
        mois: un ENTIER représentant le mois de la date à laquelle on s'intéresse
        jour: un ENTIER représentant le jour de la date à laquelle on s'intéresse

    Returns:
        Le nombre entier représentant la position de la date au mois et jour passés en paramètres
    '''
    date_reference = date(2017, 12, 31) # On retient le 31 janvier 2017 pour que le 1er janvier 2018 soit le 1er jour

    date_actuelle = date(2018, mois, jour)

    return (date_actuelle - date_reference).days


def obtenir_evenements_date_type(dictio_evenements_par_type, jour_annee, type_evenement):
    '''
    Cette fonction permet d'obtenir les évènements d'un type donné auquel une personne peut assister à une
    date passée en paramètre. Pour ce faire, la fonction commence donc par filtrer les évènements contenus dans
    le dictionnaire pour seulement s'intéresser aux évènements de même type que le paramètre type_evenement.
    Ensuite, pour chaque evenement du bon type, si le DEBUT_EVENEMENT est plus petit ou égal que jour_annee ET
    que la FIN_EVENEMENT est plus grande ou égale que jour_annee, on peut ajouter le nom de l'évènement en question à la
    liste des évènements accessibles, que l'on retourne.

    *** N.B. Si aucun évènement n'est accessible, la fonction retourne une liste vide []. ***

    Args:
        dictio_evenements_par_type: le dictionnaire des évènements formatés filtrés par leur type, dictionnaire
        jour_annee: la position du jour désiré dans l'année 2018, entier
        type_evenement: le type d'évènement recherché, string

    Returns:
        une liste contenant le nom de tous les évènements du bon type et qui sont offerts à la date
        recherchée.
    '''
    # TODO: Programmez cette fonction en retirant l'instruction pass (qui ne fait rien) et en y
    # TODO: ajoutant votre code.
    pass

def demander_jour_annee():
    '''
    Cette fonction va demander à l'usager d'entrer une date au format AAAA-MM-JJ. La saisie entrée par l'usager doit
    ensuite être traduite en entier représentant la position de la date dans l'année 2018.

    ***Vous avez déjà eu à faire un traitement similaire sur les dates contenues dans le fichier evenements.txt,
    pensez à réutiliser ce que vous avez développé !***

    ***Vous n'avez aucune validation à faire sur la saisie faite par l'usager. Si l'usager entre autre chose qu'une
    date au format AAAA-MM-JJ, c'est normal si votre programme plante.***

    Returns:
        Le nombre entier représentant la position de la date au mois et jour saisies par l'usager.
    '''
    # TODO: Programmez cette fonction en retirant l'instruction pass (qui ne fait rien) et en y
    # TODO: ajoutant votre code.
    pass


def demander_type_evenement():
    '''
    Cette fonction va demander à l'usager d'entrer le type d'évènement qui l'intéresse. La saisie de l'usager
    doit faire partie des types contenus dans la liste types_evenements. TANT QUE l'usager n'entre pas un choix
    qui est dans types_evenements, on lui indique que la saisie est invalide et qu'il doit recommencer.
    Lorsque le choix est valide, on le retourne.

    ***Aucun action n'a besoin d'être appliquée sur le saisie faite par l'usager. On est à la recherche ici
    d'un type au format string, tel que contenu dans types_evenements.***

    Returns:
        le type d'évènement choisi par l'usager, string
    '''
    # TODO: Programmez cette fonction en retirant l'instruction pass (qui ne fait rien) et en y
    # TODO: ajoutant votre code.
    pass


def affichage_evenements(evenements):
    '''
    Cette fonction va faire l'affichage de la liste des noms des évènements accessibles selon le type et la date passée
    en paramètre. Pour l'affichage, trois cas distincts sont à gérer :

    1) La liste est vide. Dans ce cas, on affiche un message disant qu'il n'y a pas d'évènement du type
    recherché à date entrée.

    2) La liste contient un seul évènement. Dans ce cas, on précise qu'un seul évènement est accessible et
    on affiche son nom.

    3) La liste contient plus d'un évènement. Dans ce cas, on indique le nombre d'évènements accessibles et on
    les affiche tous, chacun sur une ligne différente.

    Args:
        evenements: la liste des noms des évènements accessibles
    '''
    # TODO: Programmez cette fonction en retirant l'instruction pass (qui ne fait rien) et en y
    # TODO: ajoutant votre code.
    pass


def demander_terminaison():
    '''
    Cette fonction va demander à l'utilisateur s'il désire terminer les interactions avec votre programme.
    Vous devez utiliser le format présenté dans l'énoncé du tp où la saisie de l'usager doit être 'o' pour
    que les interactions continuent, sinon le programme s'arrête.

    Returns:
        False, si la saisie de l'utilisateur est 'o' (donc qu'il ne veut pas terminer), True sinon.
    '''
    # TODO: Programmez cette fonction en retirant l'instruction pass (qui ne fait rien) et en y
    # TODO: ajoutant votre code.
    pass


def interactions_usager(dictio_evenements_par_type):
    '''
    ***Cette fonction a déjà été implémentée pour vous.***

    Cette fonction représente la procédure des interactions avec l'usager. Elle fait les différents appels aux
    fonctions que vous aurez implémentées. Regardez attentivement l'ordre dans lequel vos fonctions sont appelées
    pour bien comprendre l'exécution du programme.

    Args:
        dictio_evenements_par_type: le dictionnaire d'évènements formatés filtrés par leur type
    '''
    terminer = False

    while not terminer:
        print()
        print()
        jour_annee = demander_jour_annee()

        type_evenement = demander_type_evenement()

        evenements = obtenir_evenements_date_type(dictio_evenements_par_type, jour_annee, type_evenement)

        affichage_evenements(evenements)

        terminer = demander_terminaison()


if __name__ == "__main__":
    '''
    Le main de votre programme. Votre programme se sépare en deux parties : la création du dictionnaire
    d'évènements à partir de evenements.txt (formattage des donnees) et les interactions avec l'usager, contenues dans 
    interactions_usager().
    
    ***Vous n'avez rien à ajouter ici pour faire fonctionner votre programme.***
    '''
    dictio_evenements_par_type = creer_dictio()

    print("Formattage terminé")

    interactions_usager(dictio_evenements_par_type)
