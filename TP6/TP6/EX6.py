
# Exercice 8 : Tests Unitaires pour les Exceptions
import unittest
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
def convert_to_int(value):
  
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Impossible de convertir '{value}' en entier.")
def read_file(filename):
    
    try:
        file = open(filename, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        error_message = f"Error: The file '{filename}' does not exist."
        print(error_message)
       
    finally:
        try:
            file.close()
        except NameError:
            pass
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
def process_input(user_input):
   
    try:
        number = int(user_input)
        result= 10/number
        print(f"le resultat de l'affichage est : {result}")
    
    except ValueError:
        print(f"Error: '{user_input}' C nest pas un entier.")
    except ZeroDivisionError:
        print("Error: Division par zero est impossible.")
         

class TestExceptions(unittest.TestCase):

    def test_safe_division(self):
        with self.assertRaises(ZeroDivisionError):
            safe_division(10, 0)

    def test_convert_to_int(self):
        with self.assertRaises(ValueError):
            convert_to_int("abc")

    def test_read_file(self):
        with self.assertRaises(FileNotFoundError):
            read_file("non_existent_file.txt")

    def test_set_age(self):
        with self.assertRaises(NegativeAgeError):
            set_age(-5)

    def test_process_input_value_error(self):
        with self.assertRaises(ValueError):
            process_input("not_a_number")

    def test_process_input_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            process_input(0)

if __name__ == "__main__":
    unittest.main()
