#SILENCIANDO UN ERROR
def dividir(dividendo, divisor):
    resultado = 0
    try:
        resultado = dividendo / divisor
    except ZeroDivisionError as zde:
        pass #Estamos silenciando el error
    return resultado

print(dividir(3,0))

#NO SILENCIANDO EL ERROR (SE TRATA Y SE PROPAGA)
def dividir_sin_silenciar(dividendo, divisor):
    resultado = 0
    try:
        resultado = dividendo / divisor
    except ZeroDivisionError as zde:
        print("Esto es log del error:",zde)
        raise zde
    return resultado

try:
    print(dividir_sin_silenciar(3,0))
except ZeroDivisionError as zde:
    print("Tratamiento final de la excepción:", zde)