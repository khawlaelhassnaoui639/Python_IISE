import json

# Dictionnaire contenant les informations sur les étudiants
etudiants = {
    "etudiants": [
        {"nom": "Ali", "age": 20, "note": 15.5},
        {"nom": "Sarah", "age": 22, "note": 16.8},
        {"nom": "Omar", "age": 21, "note": 14.2}
    ]
}
# Enregistrement du dictionnaire dans un fichier JSON
with open("etudiants.json", "w", encoding="utf-8") as fichier:
    json.dump(etudiants, fichier, ensure_ascii=False, indent=4)

print("Les informations des étudiants ont été enregistrées dans 'etudiants.json'.")
# Lecture du fichier JSON
with open("etudiants.json", "r", encoding="utf-8") as fichier:
    donnees = json.load(fichier)  # Charger le contenu du fichier JSON dans une variable

# Affichage des informations des étudiants
for etudiant in donnees["etudiants"]:
    print(f"Nom : {etudiant['nom']}, Âge : {etudiant['age']}, Note : {etudiant['note']}")
