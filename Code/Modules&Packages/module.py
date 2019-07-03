from zero import *
import user.structure
from user.greetings import despedida, funcion
from mathe.operations import media, suma, variable_functions
import user.message as ok
import numpy as np
a = 5
b = 7

lista = user.structure.devuelve_lista()
print(lista)

tupla = user.structure.tupla
print(tupla)

print(media(1, 2, 3, 4, 5))
funcion()

print(variable_functions)
print(suma(a, b))

despedida()
ok.mensaje()