#!/opt/conda/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

class Timescale_new(object):
	"""
    The base class for any kind of set.
	"""
	def __init__(self, ts = None, name = None):
		self.ts = ts
		self.name = name

	def input_closed_set(self):
		pass
		# try:
		# 	iterator = iter(TS9.ts)
		# except TypeError:
		# 	# TODO: Obtener su clausura.
		# 	print("Desea definir esta nueva escala de tiempo.")
		# Conjuetura de Collatz para obtener conjuntos cerrados.
		# else:
		# 	# TODO: En el caso cerrado.
		# 	print("T es un conjunto cerrado.")

	def __str__(self):
		return f"¡La escala de tiempo {self.ts}, {self.name}, fue construida con éxito!"


class Timescale(object):
	"""Objeto matemático llamado escala de tiempo.

	Métodos:
		constructor(v0): fija el valor inicial.
		value(t): calcula la altura como función de t.
		formula(): imprime fuera la fórmula para la altura.

	Atributos de datos:
		v0: la velocidad inicial de la bola (tiempo 0).
		g: aceleración de la gravedad.

	Examples:
	========

	>>> from timescale import Timescale as tsc
	>>> intervalo = [0, 1, 2, 3, 4, 5, 6, 7]
	>>> nombre = 'documentation example'
	>>> t1 = tsc(intervalo, nombre)
	"""
	def __init__(self, ts, nombre = 'sin nombre'):
		self.ts = ts
		self.name = nombre

		"""
		Los siguientes dos miembros de datos del diccionario se han utilizado para la
		memorización de las funciones g_k y h_k de esta clase.
		"""
		self.memo_g_k = {}
		self.memo_h_k = {}

		"""
		El siguiente miembro de dato permite a los usuarios acceder a las funciones de la interfaz matplotlib.pyplot.
		
		Esto significa que un usuario tiene más control sobre la funcionalidad de trazado de esta clase.
		
		Por ejemplo, las funciones xlabel e ylabel de la interfaz pyplot se pueden configurar a través
		de este miembro de datos.
		
		Luego, cuando llame las funciones plot() o scatter() de esta clase (a través de plt.show()),
		xlabel y ylabel mostrarán lo que el usuario las configure.
		
		Consulte este recurso para obtener una lista de las funciones disponibles:
		https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html
		"""
		self.plt = plt
		"""
		El siguiente código valida la escala de tiempo especificada por el usuario para garantizar que no haya
		superposiciones, como por ejemplo:
			* un punto dado más de una vez.
			* un punto que se incluye en un intervalo.
			* un punto que es el valor inicial o el valor final de un intervalo.
			* un intervalo dado más de una vez.
			* intervalos superpuestos.
		Si se detecta que una escala de tiempo no es válida, se generará una excepción con el mensaje correspondiente
		que describe la causa de la invalidez.
		"""
		for listItem in ts:
			if isinstance(listItem, list):
				if len(listItem) > 2:
					raise Exception("Declaración de escala de tiempo no válida: no puede tener un intervalo con más de un valor inicial y uno final.")

				if len(listItem) < 2:
					raise Exception("Declaración de escala de tiempo no válida: un intervalo debe tener un valor inicial y un valor final.")

				if listItem[0] > listItem[1]:
					raise Exception("Declaración de escala de tiempo no válida: no puede tener un intervalo en el que el valor final sea menor que el valor inicial.")

				if listItem[0] == listItem[1]:
					raise Exception("Declaración de escala de tiempo no válida: no puede tener un intervalo en el que el valor inicial y el valor final sean iguales (dicho intervalo debe declararse como un punto).")

			for listItemToCompare in ts:
				if listItem == listItemToCompare and listItem is not listItemToCompare:
					raise Exception("Declaración de escala de tiempo no válida: no puede incluir el mismo punto o intervalo más de una vez.")

				if listItem is not listItemToCompare:
					if isinstance(listItem, list) and isinstance(listItemToCompare, list):
						if (listItem[0] >= listItemToCompare[0] and listItem[0] <= listItemToCompare[1]) or (listItem[1] >= listItemToCompare[0] and listItem[1] <= listItemToCompare[1]):
							raise Exception("Declaración de escala de tiempo no válida: no puede haber intervalos superpuestos.")

					if isinstance(listItem, list) and not isinstance(listItemToCompare, list):
						if listItemToCompare >= listItem[0] and listItemToCompare <= listItem[1]:
							raise Exception("Declaración de escala de tiempo no válida: no puede declarar un punto que se incluye en un intervalo (no puede declarar un valor más de una vez).")

					if not isinstance(listItem, list) and isinstance(listItemToCompare, list):
						if listItem >= listItemToCompare[0] and listItem <= listItemToCompare[1]:
							raise Exception("Invalid timescale declaration: you cannot declare a point that is included in an interval (you cannot declare a value more than once).")

	def __str__(self):
		return "¡La escala de tiempo {}, {}, fue construida con éxito!".format(self.ts, self.name)


def integers(a, b):
	"""
	Create the time scale of integers {x : a <= x <= b}
	"""
	return Timescale(list(range(a,b+1)),'integers from '+str(a)+' to '+str(b))


def quantum(q, m, n):
	"""
	Create the time scale of quantum numbers of form {q^k:k=m,m+1,...,n}
	only does q^(X) where X={0,1,2,3,...} at the moment
	"""
	return Timescale([q**k for k in range(m,n)], 'quantum numbers '+str(q)+'^'+str(m)+' to '+str(q)+'^'+str(n))