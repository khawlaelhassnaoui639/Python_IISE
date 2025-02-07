try:
    # Tentative d'ouverture du fichier en mode lecture
    with open("inexistant.txt", "r", encoding="utf-8") as fichier:
        contenu = fichier.read()
        print("Contenu du fichier :")
        print(contenu)
except FileNotFoundError:
    # Gestion de l'erreur si le fichier n'existe pas
    print("Erreur : Le fichier 'inexistant.txt' n'existe pas.")
except Exception as e:
    # Gestion d'autres erreurs inattendues
    print(f"Une erreur inattendue est survenue : {e}")
