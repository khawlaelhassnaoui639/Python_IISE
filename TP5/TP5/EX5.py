import os

# Étape 1 : Renommer le fichier
ancien_nom = "phrases.txt"
nouveau_nom = "anciennes_phrases.txt"

try:
    # Renommer le fichier
    os.rename(ancien_nom, nouveau_nom)
    print(f"Le fichier '{ancien_nom}' a été renommé en '{nouveau_nom}'.")
except FileNotFoundError:
    print(f"Le fichier '{ancien_nom}' n'existe pas.")
except Exception as e:
    print(f"Une erreur est survenue lors du renommage : {e}")

# Étape 2 : Supprimer le fichier renommé
try:
    os.remove(nouveau_nom)
    print(f"Le fichier '{nouveau_nom}' a été supprimé.")
except FileNotFoundError:
    print(f"Le fichier '{nouveau_nom}' n'existe pas.")
except Exception as e:
    print(f"Une erreur est survenue lors de la suppression : {e}")
