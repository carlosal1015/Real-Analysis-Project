def suma(a, b):
	return a + b

def media(*numeros):
	media = 0
	for i in numeros:
		media = media + i
	return media / len(numeros)

# El * indica que podemos emplear tantos números como argumentos queramos (finito).

variable_functions = 2
print("Módulo operaciones")