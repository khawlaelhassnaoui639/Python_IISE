def somme_liste(liste):
    som=0
    for nbr in liste:
        som+=nbr
    return som
list1=[1,8,9,10]
print("la somme des element de liste est:", somme_liste(list1))