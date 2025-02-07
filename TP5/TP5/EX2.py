# Demander à l'utilisateur d'entrer trois phrases
print("Veuillez entrer trois phrases :")
phrases = []

for i in range(3):
    phrase = input(f"Phrase {i+1} : ")
    phrases.append(phrase)


# Enregistrer les phrases dans un fichier nommé "phrases.txt"
with open("phrases.txt", "w", encoding="utf-8") as fichier:
    for phrase in phrases:
        fichier.write(phrase + "\n")

print("Les phrases ont été enregistrées dans 'phrases.txt'.")
# Demander à l'utilisateur s'il souhaite ajouter d'autres phrases
while True:
    ajouter = input("Souhaitez-vous ajouter d'autres phrases ? (oui/non) : ").strip().lower()
    if ajouter == "oui":
        nouvelle_phrase = input("Entrez une phrase à ajouter : ")
        with open("phrases.txt", "a", encoding="utf-8") as fichier:  # Mode 'a' pour ajouter
            fichier.write(nouvelle_phrase + "\n")
        print("Phrase ajoutée avec succès !")
    elif ajouter == "non":
        print("Fin du programme.")
        break
    else:
        print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")