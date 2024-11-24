# Gestionnaire de tâches

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Init~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import json
import time

fichier = "taches.json"

# Lecture du fichier JSON ou initialisation si vide
try:
    with open(fichier, 'r', encoding='utf-8') as f:
        donnees = json.load(f)
        liste = donnees.get("taches", [])  # Charger la liste des tâches
except FileNotFoundError:
    # Si le fichier n'existe pas, on initialise une structure par défaut
    donnees = {"taches": []}
    liste = donnees["taches"]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Zone des définitions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def sauvegarder():
    """Sauvegarde les tâches dans le fichier JSON."""
    donnees["taches"] = liste  # Met à jour la clé "taches"
    with open(fichier, 'w', encoding='utf-8') as f:
        json.dump(donnees, f, ensure_ascii=False, indent=4)
    print("Les modifications ont été sauvegardées.")

def suppr_taches():
    """Supprime une tâche de la liste."""
    print("Voici vos tâches :", liste)
    tache = input("Écrivez la tâche à supprimer : ").strip()
    if tache in liste:
        liste.remove(tache)
        print("Tâche supprimée. Voici la liste mise à jour :", liste)
        sauvegarder()  # Sauvegarder après modification
    else:
        print(f"La tâche '{tache}' n'est pas dans la liste.")

def ajouter_taches():
    """Ajoute une tâche à la liste."""
    print("Voici vos tâches :", liste)
    tache = input("Écrivez la tâche à ajouter : ").strip()
    if tache:  # Vérifie que la tâche n'est pas vide
        liste.append(tache)
        print("Tâche ajoutée. Voici la liste mise à jour :", liste)
        sauvegarder()  # Sauvegarder après modification
    else:
        print("La tâche ne peut pas être vide.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Le Main~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("Bienvenue dans votre gestionnaire de tâches")

while True:
    print("\n~~~~~~~~~~~~~~~~ Menu ~~~~~~~~~~~~~~~~~~")
    print("| Tapez : 0 pour arrêter le programme  |")
    print("| Tapez : 1 pour ajouter une tâche     |")
    print("| Tapez : 2 pour supprimer une tâche   |")
    print("| Tapez : 3 pour visionner vos tâches  |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # Sélection du mode :
    try:
        choix = int(input("Tapez 0, 1, 2 ou 3 selon votre choix : "))
    except ValueError:
        print("Veuillez entrer un nombre valide (0, 1, 2 ou 3).")
        continue

    if choix == 0:
        print("Arrêt du programme.")
        break
    elif choix == 1:
        print("Vous avez choisi d'ajouter une tâche.")
        ajouter_taches()
        time.sleep(0.5)
    elif choix == 2:
        print("Vous avez choisi de supprimer une tâche.")
        suppr_taches()
        time.sleep(0.5)
    elif choix == 3:
        print("Vous avez choisi de visionner vos tâches.")
        print("Voici votre liste :", liste)
        time.sleep(1.5)
    else:
        print("Veuillez taper UNIQUEMENT 0, 1, 2 ou 3 selon votre choix.")
        time.sleep(1.5)
