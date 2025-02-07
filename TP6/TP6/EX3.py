# Exercice 3 : Lecture de Fichier
   
   
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
