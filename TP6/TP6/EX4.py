# Exercice 4 : Exceptions Personnalisées
class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError(f"Invalid age: {age}. Age cannot be negative.")
    else:
        print(f"age est: {age}")
    return age
try:
    set_age(18)
except NegativeAgeError as e:
 print(e)
