#Mala práctica el uso de global

def calcular(valor_1, valor_2):
    global resultado
    resultado = valor_1 + valor_2

calcular(10, 15)
print(resultado)