import csv

# Étape 1 : Créer le fichier CSV "contacts.csv" avec des données
with open("file.csv", "w", newline="", encoding="utf-8") as fichier:
    writer = csv.writer(fichier)
    # Écriture de l'en-tête
    writer.writerow(["Nom", "Âge", "Ville"])
    # Écriture des données
    writer.writerows([
        ["Alice", 30, "Paris"],
        ["Bob", 25, "Lyon"],
        ["Charlie", 35, "Marseille"],
        ["Diana", 28, "Toulouse"],
        ["Edward", 40, "Nice"]
    ])

print("Fichier 'contacts.csv' créé avec succès.")

# Étape 2 : Lire le fichier et afficher les informations
with open("contacts.csv", "r", encoding="utf-8") as fichier:
    reader = csv.DictReader(fichier)
    print("\nInformations des contacts :\n")
    for ligne in reader:
        print(f"Nom : {ligne['Nom']}, Âge : {ligne['Âge']}, Ville : {ligne['Ville']}")
