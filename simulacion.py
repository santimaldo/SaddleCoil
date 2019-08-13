class Simulacion :
	'''Esta clase contiene la información de la simulación realizada en COMSOL.

Atributos
----------

 parametros: array_like
    arreglo de parametros usados para la simulacion. COMPLETAR DOCUMENTACION.

resultados : array_like
    resultados de la simulacion. COMPLETAR DOCUMENTACION.
'''
	def __init__(self) :
		self.archivo = None # string
		self.parametros = None # array_like
		self.resultados = None # array:like
		pass
	def set_resultados (self) :
		""" Método utilizado para extraer los resultados de la simulación del `archivo`, y los carga en el atributo `parametros`. """
		# returns 
		pass
	def set_parametros (self) :
		""" Método utilizado para extraer los parámetros de la simulación del `archivo`, y los carga en el atributo `parametros`. """
		# returns 
		pass
