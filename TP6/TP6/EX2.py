
def convert_to_int(value):
  
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Impossible de convertir '{value}' en entier.")
    

print(convert_to_int("khawla"))