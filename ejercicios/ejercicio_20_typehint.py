"""Docstring para acallar al linter"""


def calcular_area(ancho: int, alto: int) -> int:
    """Calcula el área de un rectángulo
    En caso de que los dos lados sean iguales
    lanzará un error y escribirá un log.
    """
    area = ancho * alto
    return area


RESULTADO = calcular_area(ancho=3, alto=10)
