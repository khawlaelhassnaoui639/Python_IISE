def statistiques_fichier(nom_fichier):
    try:
        # Ouvrir le fichier en mode lecture
        with open("fichier.txt", "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")
    else:        
        # Calculer le nombre total de lignes
        nombre_lignes = len(lignes)

        # Calculer le nombre total de mots et de caractères
        nombre_mots = 0
        nombre_caracteres = 0
        for ligne in lignes:
            nombre_mots += len(ligne.split())  # Divise chaque ligne en mots
            nombre_caracteres += len(ligne)   # Compte tous les caractères (espaces inclus)

        # Afficher les statistiques
        
        print(f"- Nombre total de lignes     : {nombre_lignes}")
        print(f"- Nombre total de mots       : {nombre_mots}")
        print(f"- Nombre total de caractères : {nombre_caracteres}")

# Appeler la fonction avec un fichier exemple
nom_fichier = "fichier.txt"  
statistiques_fichier(nom_fichier)
