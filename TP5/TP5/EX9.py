import csv
import os

# Nom du fichier CSV
fichier_contacts = "contacts.csv"

# Initialiser le fichier CSV s'il n'existe pas
if not os.path.exists(fichier_contacts):
    with open(fichier_contacts, "w", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(["Nom", "Téléphone", "Email"])  # En-têtes

# Fonction pour afficher le menu
def afficher_menu():
    print("\nGestion des contacts")
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Rechercher un contact par nom")
    print("4. Supprimer un contact")
    print("5. Quitter")

# Fonction pour ajouter un contact
def ajouter_contact():
    nom = input("Nom : ")
    telephone = input("Téléphone : ")
    email = input("Email : ")
    with open(fichier_contacts, "a", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerow([nom, telephone, email])
    print(f"Contact ajouté : {nom}")

# Fonction pour afficher tous les contacts
def afficher_contacts():
    with open(fichier_contacts, "r", encoding="utf-8") as fichier:
        reader = csv.reader(fichier)
        contacts = list(reader)
        if len(contacts) > 1:  # Vérifie si des contacts existent (hors en-têtes)
            print("\nListe des contacts :")
            for i, contact in enumerate(contacts[1:], start=1):  #  c pour Sauter les en-têtes
                print(f"{i}. Nom : {contact[0]}, Téléphone : {contact[1]}, Email : {contact[2]}")
        else:
            print("Aucun contact trouvé.")

# Fonction pour rechercher un contact par nom
def rechercher_contact():
    nom_recherche = input("Entrez le nom à rechercher : ").lower()
    with open(fichier_contacts, "r", encoding="utf-8") as fichier:
        reader = csv.reader(fichier)
        contacts = [contact for contact in reader if contact and contact[0].lower() == nom_recherche]
        if contacts:
            print("\nRésultat de la recherche :")
            for contact in contacts:
                print(f"Nom : {contact[0]}, Téléphone : {contact[1]}, Email : {contact[2]}")
        else:
            print("Aucun contact trouvé avec ce nom.")

# Fonction pour supprimer un contact
def supprimer_contact():
    nom_suppression = input("Entrez le nom du contact à supprimer : ").lower()
    with open(fichier_contacts, "r", encoding="utf-8") as fichier:
        reader = csv.reader(fichier)
        contacts = list(reader)

    contacts_restants = [contact for contact in contacts if contact and contact[0].lower() != nom_suppression]

    if len(contacts_restants) == len(contacts):
        print("Aucun contact trouvé avec ce nom.")
    else:
        with open(fichier_contacts, "w", newline="", encoding="utf-8") as fichier:
            writer = csv.writer(fichier)
            writer.writerows(contacts_restants)
        print(f"Contact '{nom_suppression}' supprimé.")

# Boucle principale
while True:
    afficher_menu()
    choix = input("Choisissez une option : ")

    if choix == "1":
        ajouter_contact()
    elif choix == "2":
        afficher_contacts()
    elif choix == "3":
        rechercher_contact()
    elif choix == "4":
        supprimer_contact()
    elif choix == "5":
        print("Au revoir !")
        break
    else:
        print("Option invalide. Veuillez réessayer.")
