from timescale import Timescale as tsc
import chalk
import emoji

def welcome(func):
	def wrapper_welcome():
		ascii_art_1 = """
  _____ _                                _      
 |_   _(_)_ __ ___   ___   ___  ___ __ _| | ___ 
   | | | | '_ ` _ \ / _ \ / __|/ __/ _` | |/ _ \\
   | | | | | | | | |  __/ \__ | (_| (_| | |  __/
   |_| |_|_| |_| |_|\___| |___/\___\__,_|_|\___|"""
		ascii_art_2 = """
,--,--'                        .      
`- | . ,-,-. ,-.   ,-. ,-. ,-. |  ,-. 
 , | | | | | |-'   `-. |   ,-| |  |-' 
 `-' ' ' ' ' `-'   `-' `-' `-^ `' `-'"""
		message = "The timescalecalculus python library."
		star = emoji.emojize(':star:', use_aliases=True)
		print(chalk.green(ascii_art_1, bold = True))
		print(chalk.yellow(ascii_art_2, bold = True))
		print(chalk.magenta(3*star + " " + message + 3*star))
		print(chalk.cyan("¡Bienvenido matemático!"))
		func()
	return wrapper_welcome

# Generador en ascii-code
# http://patorjk.com/software/taag/#p=display&h=3&f=Stampatello&t=Time%20scale

@welcome
def show_status():
	success = chalk.green(emoji.emojize(':heavy_check_mark:', use_aliases=True).center(10, " ") * 5)
	error = chalk.red(emoji.emojize(':x:', use_aliases=True).center(10, " ") * 5)

	if hasattr(F1, '_ts') and hasattr(F1, '_name'):
		print(success)
		print(chalk.green("¡Escala de tiempo inicializada!"))
		# TODO: Imprimir los datos de la escala de tiempo.
		# TODO: Emplear una tupla en vez de una lista.
		print(f"Datos de la escala de tiempo:")
		print(f"Su nombre es {F1._name}.")
		print(f'Conjunto T = {{{", ".join(map(str, F1._ts))}}}.')
	else:
		print(error)
		print(chalk.red("Se ha producido un error."))
		# TODO: Proporcionar una ayuda. Por ejemplo mencionar algunos conjuntos cerrados.


F1 = tsc([0, 1, 2, 3, 4, 5, 6, 7], 'documentation example')