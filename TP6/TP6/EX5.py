# Exercice 5 : Multi-Exceptions
def process_input(user_input):
   
    try:
        number = int(user_input)
        result= 10/number
        print(f"le resultat de l'affichage est : {result}")
    
    except ValueError:
        print(f"Error: '{user_input}' C nest pas un entier.")
    except ZeroDivisionError:
        print("Error: Division par zero est impossible.")

    
process_input("20") 
process_input("0")    
