
# Mal
# lista = [ 1, 2, 4]

# Bien
lista = [1, 2, 4]

# Mal
# diccionario = {'clave' : 1}

# Bien
diccionario = {'clave': 1}

# Mal
# print("Hola" , "amig@")

# Bien
print("Hola", "amig@")

cadena = "Esto es una cadena de texto"

# Mal
# trozo_cadena = cadena[ 0 : 4]

# Bien
trozo_cadena = cadena[0:4]  # Mi favorita
trozo_cadena = cadena[0: 4]


# Mal
# x      =     5   +  3

# Bien
x = 5+3

# Bien (recomendable)
x = 5 + 3

# Mal
# x = (5 - 8) * (3 + 2)

# Bien
x = (5 - 8) * (3 + 2)
x = 5 * 8 + 3

# Bien (a discreción)
x = (5-8) * (2-1)
x = 5*8 + 3

# Operador = como asignación
# x=5 # Mal
x = 5  # Ok


# Operador = como asignador de valor por defecto en funciontes/métodos

# def sumar(s1 = 3, s2 = 8): # Mal
#    pass

def sumar(s1=3, s2=8):  # Bien
    pass
