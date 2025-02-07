import os
import shutil

# Étape 1 : Créer un fichier texte
with open("journal.txt", "w", encoding="utf-8") as fichier:
    fichier.write("Ligne 1 : Ceci est un journal.\n")
    fichier.write("Ligne 2 : Aujourd'hui, il fait beau.\n")
    fichier.write("Ligne 3 : Python est amusant.\n")
print("Le fichier 'journal.txt' a été créé.")

# Étape 2 : Copier le fichier
shutil.copy("journal.txt", "journal_copie.txt")
print("Le fichier 'journal.txt' a été copié en 'journal_copie.txt'.")

# Étape 3 : Déplacer le fichier dans un dossier
os.makedirs("archives", exist_ok=True)# creer un répértoire

shutil.move("journal_copie.txt", "archives/journal_copie.txt")
print("Le fichier 'journal_copie.txt' a été déplacé dans le dossier 'archives'.")
