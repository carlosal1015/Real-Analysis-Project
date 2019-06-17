"""
Ejemplos de la página web
http://timescalewiki.org/index.php/Timescalecalculus_python_library_documentation
"""
from timecalculus import timescalecalculus as tsc

ts = tsc.timescale([2, 3, 5, 7, 11, 13, 17], 'primes')

print(ts.dexp_p(lambda x: 1, 5, 2))

print(ts.dexp_p(lambda x: 1, 11, 2))

print(ts.dexp_p(lambda x: x, 5, 2))