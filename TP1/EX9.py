#Écrivez une fonction `analyse_texte(texte)` qui prend une chaîne de caractères, compte le nombre de mots et retourne un dictionnaire avec le nombre de mots et le nombre de caractères.

def analyse_texte(texte):
    Dict={"mots":1,"caracteres":0}
    if len(texte)==0:
        return "chaine vide"
    else:
        for i in texte:
            if i == ' ':
                Dict["mots"]+=1
            else:
                Dict["caracteres"]+=1
    return Dict

print(analyse_texte("there is no ctrl Z in life"))

