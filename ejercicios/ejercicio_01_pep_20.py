#(1)Lo bonito es mejor que lo feo

#FEO
'''
from math import sqrt
sidea = float(input("Longitud del lado 'a':"))
sideb = float(input("Longitud del lado 'b':"))
sidec = sqrt(sidea**2+sideb**2)
print("La longitud de la hipotenusa es",sidec)
'''

#BONITO
'''
from math import sqrt

side_a = float(input("Longitud del lado 'a':"))
side_b = float(input("Longitud del lado 'b':"))
hypotenuse = sqrt(side_a**2 + side_b**2)

print("La longitud de la hipotenusa es",sidec)
'''

#(2)Explícito es mejor que implícito
'''
#Implícito
from fruit import *

apples(2, 3.45)

#Explícito
from fruit import apples, bananas

apples(quantity=2, prices=3.45)
'''

#(3)Lo simple es mejor que lo complejo
#No utilizar la orientación a objetos si no es necesario
#Complejo
import heapq

numbers = [-1, 12, -5, 0, 7, 21, 15, 1]
heapq.heapify(numbers)

sorted_numbers = []

while numbers:
    sorted_numbers.append(heapq.heappop(numbers))

print(sorted_numbers)

#Simple
numbers = [-1, 12, -5, 0, 7, 21, 15, 1]
numbers.sort()

print(numbers)

#(4) Lo complejo es mejor que lo complicado

#(5) El código plano es mejor que el código anidado
#A partir de 3 niveles de anidación el código resulta difícil de leer.
#A partir de 3 niveles de anidación --> Refactorizar el código

#(6) El código disperso es mejor que el código denso

#Denso
x = 1
if x == 1 : print("Hola")

#Disperso:
x = 1
if x == 1:
    print("Hola")

#(7) La legibilidad es importante

#Menos legible
def f(i):
    l = i + (0.08 * i)
    return l

#Más legible
IMPUESTO = 0.08
def calcular_importe_neto(precio_bruto):
    precio_neto = precio_bruto + (IMPUESTO * precio - bruto)
    return precio_neto

# (8) Los casos especiales no son lo suficientemente especiales para romper las reglas
# (9) ...aunque la practicidad supera a la pureza
# Si número de caracteres excede el máximo recomendado y esto favorece la legilidad 
# y la comprensión del código, se puede exceder el máximo.
# Si estamos trabajando en un proyecto que 'no cumple las reglas'.
# Ante este tipo de notación (CamelCase), se recomienda continuar con ella
def calcularImporte(importeUnitario, numeroUnidades):
    importeTotal = importeUnitario * numeroUnidades

# (10) Lo errores nunca deberían pasar desapercibidos...
# (11) A menos que se silencien explícitamente

#Silencia el error (no produce un error pero sí el mal resultado)
number = input("Enter a number:")
multiply_number_by_two = number * 2
print("Resultado:", multiply_number_by_two)

#No silencia el error
number = int(input("Enter a number:"))
multiply_number_by_two = number * 2
print("Resultado:", multiply_number_by_two)

# (12) Ante la ambigüedad, rechaza la tentación de adivinar
# No suponer que el programa funciona --> Hacer pruebas.
# Asignar de nombres autoexplicativos.
# Documentar aquello que pueda resultar difícil de comprender.
# Leer el código después de hacerlo para comprobar que es entendible.

# (13) Debería haber una forma obvia de hacerlo, preferiblemente solo una.
# (14) Aunque puede que esa forma no sea obvia al principio (a menos que seas holandés)

# (15) Ahora es mejor que nunca.
# (16) Aunque nunca es mejor que ahora mismo.
# Si tienes una solución ahora, la implementas.
# Como no existe la perfección, no la persigues (ahora es mejor que nunca).
# No liberar el código hasta que no esté listo (no sólo que lo parezca).

# (17) Si la implementación es difícil de explicar, es un mala idea.
# (18) Si la implementación es fácil de explicar, PUEDE que sea una buena idea.

# (19) Los espacios de nombres son una buena idea ¡Hagamos más de eso!