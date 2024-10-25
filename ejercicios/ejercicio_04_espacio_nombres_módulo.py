from instrumentos import guitarras

def fender():
    print("Módulo ejercicio_04_ambito_global, función fender")

def ibanez():
    print("Módulo ejercicio_04_ambito_global, función ibanez")

guitarras.fender()
fender()

guitarras.ibanez()
ibanez()