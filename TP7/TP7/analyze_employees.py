# Importer la bibliothèque Pandas
import pandas as pd

# Lire le fichier CSV
df = pd.read_csv('employees.csv')

# Afficher les cinq premières lignes du dataframe
print("Les 5 PREMIERS lignes :")
print(df.head())

# Calculer la moyenne de l'âge des employés
average_age = df['age'].mean()

# Afficher la moyenne d'âge
print(f"\nLa moyenne d'âge des employés est : {average_age:.2f} ans")