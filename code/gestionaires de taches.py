
#gestionaire de taches

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Init~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import json
import time
liste = []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Zone des definitions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def suppr_taches ():
    print(liste)
    tache=str(input("ecrivez la tache à supprimer: "))
    if tache in liste:
        liste.remove(tache)
        print("voilà le résultat :",liste)
    else:
        print(f"La tâche '{tache}' n'est pas dans la liste.")

def ajouter_taches ():
    print(liste)
    tache=str(input("ecriver la tache à ajouter: "))
    liste.append(tache)
    print("voilà le résultat :",liste)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~le Main~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#menu :

print("bienvenue dans votre gestionaire de taches")

while True:

    print("~~~~~~~~~~~~~~~~ menu: ~~~~~~~~~~~~~~~~~~")
    print("| tapper: 0 pour arreter le programme   |")
    print("| tapper: 1 pour ajouter une tache      |")
    print("| tapper: 2 suppimer une tache          |")
    print("| tapper: 3 pour visioner vos taches    |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#sélection du mode :

    choix=int(input("tapper 0, 1, 2 ou 3 selon votre choix "))

    if choix==0:
        print("arret du programme")
        exit()
    elif choix==1:
        print("vous avez choisi d'ajouter une tache")
        ajouter_taches ()
        time.sleep(0.5)
    elif choix==2:
        print("vous avez choisi de suppimer une tache")
        suppr_taches ()
        time.sleep(0.5)
    elif choix==3:
        print("vous avez choisi de visioner vos taches")
        print("voici votre liste :",liste)
        time.sleep(1.5)
    else:
        print("veuillez tapper UNIQUEMENT 0, 1, 2 ou 3 selon votre choix ")
        time.sleep(1.5)