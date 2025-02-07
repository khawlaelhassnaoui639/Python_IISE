# Ouvrir le fichier en mode lecture
with open("exemple.txt", "r", encoding="utf-8") as fichier:
    # Lire les lignes du fichier
    lignes = fichier.readlines()

# Parcourir et afficher chaque ligne avec son numéro
for numero, ligne in enumerate(lignes, start=1):
    print(f"Ligne {numero}: {ligne.strip()}")