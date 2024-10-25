'''
#No conforme con PEP8
class Motor():
    normativa_europea='EU0832X2'
    def      __init__(self,nombre):
        self.nombre=nombre
    def arrancar(self):
        print("Arrancando...")


motor=Motor("Renault")
opcion = int(input('Opción [0,1]:'))
if (opcion == 1):print ('Uno')
elif (opcion== 2):print('Dos' )
'''

# Conforme con PEP8


class Motor():
    normativa_europea = 'EU0832X2'

    def __init__(self, nombre):
        self.nombre = nombre

    def arrancar(self):
        print("Arrancando...")


motor = Motor("Renault")

opcion = int(input('Opción [0,1]:'))
if (opcion == 1):
    print('Uno')
elif (opcion == 2):
    print('Dos')
