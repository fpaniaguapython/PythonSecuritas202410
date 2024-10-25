class Motor:
    def __init__(self):
        pass

    def arrancar(self):
        print("Arrancando")

    def frenar(self):
        print("Frenando...")

    def hacer_trompo(self):
        raise NotImplementedError("El método hacer_trompo no está implementado")
        #raise DeprecationWarning("El método es obsoleto")

motor = Motor()
motor.arrancar()
motor.hacer_trompo()