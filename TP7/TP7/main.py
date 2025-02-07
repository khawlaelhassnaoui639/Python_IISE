import conversion

# Test de la fonction dollars_to_dirhams
dollars = 100
taux = 11  # Exemple de taux de conversion
dirhams = conversion.dollars_to_dirhams(dollars, taux_conversion=taux)
print(f"{dollars} dollars = {dirhams} dirhams avec un taux de conversion de {taux}.")

# Test de la fonction meters_to_kilometers
meters = 5000
kilometers = conversion.meters_to_kilometers(meters)
print(f"{meters} mètres = {kilometers} kilomètres.")
