# TypeError using try and except
from ast import operator


def palidrome(string):
    return string == string[::-1]

try:
    print(palidrome(1))
except TypeError:
    print("Solo se puede ingresar Strings")


# ValueError using raise
def palidrome(string):
    
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacia")
        return string == string[::-1]
    
    except ValueError as ve:
        print(ve)
        return False

try:
    print(palidrome(""))
except TypeError:
    print("Solo se puede ingresar Strings")


# Using the word finally:

# try:
#     f = open("archivo.txt")
#     # hacer diferentes cosas con nuestro archivo
# finally:
#     f.close()