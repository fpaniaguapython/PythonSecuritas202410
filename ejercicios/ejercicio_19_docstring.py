class Prueba:
    """
    Soy el docstring de una clase de prueba.
    Otra línea.
    Otra línea.
    Otra línea "se pueden introducir comillas".
    También 'comillas simples'.
    """

    def __init__(self, nombre: str, longitud: int):
        self.nombre = nombre
        self.longitud = longitud

    def metodo_publico(self):
        """Soy el docstring de un método público"""
        self.__metodo_privado()

    def __metodo_privado(self):
        """Soy el docstring de un método privado"""


def saludar(nombre: str, idioma: str):
    """
    Muestra un saludo por pantalla.

    Parámetros:
    -----------
    nombre: str
        El nombre de la persona a saludar
    idioma: str
        El idioma en el que va a mostrar el saludo
    """
    print(f'Hola {nombre} en {idioma}')


saludar("Raúl", "Japonés")
prueba = Prueba('Mesa', 100)
prueba.metodo_publico()
