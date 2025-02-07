import logging

# Exercice 1 : Division par Zéro
def safe_division(a, b):
   
    try:
        result = a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Division par ezro est impossible.")
    else:
        print("la devision a ete effectuer avec succes")
        return result
    finally:
        print(" l'execution de cette fonction est fini .") 