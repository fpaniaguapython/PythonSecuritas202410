# Aquí iria el docstring
# Primero los import de la biblioteca estándar
# Segundo los import de bibliotecas de terceros
# Por último los import de módulos propios
# Los bloques anteriores se separan por espacios en blanco
import math
import socket

import beautifulsoup4
import autopep8

import ejercicio_01_pep_20

# Mal
import sys
import os

# Bien
import smtplib
import socketserver

# Bien
from random import gauss, lognormvariate

# Imports absolutos (BIEN)
from instrumentos.materiales.materials import Material

# No se recomienda el uso de comodines (MAL)
from crypt import *
