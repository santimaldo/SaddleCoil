# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:11:20 2019

@author: santi
"""

import numpy as np
from scipy.interpolate import interp1d
# mis modulos:
from radiofrecuencia import Radiofrecuencia
from magnetizacion import Magnetizacion
from nutacion import Nutacion
from senal import Senal


class Simulacion:
    """
    Esta clase contiene la información de la simulacion realizada en COMSOL.
    Ademas, los metodos para realizar el analisis
    
    Attributes
    ----------
    archivo : string
        direccion y nombre del archivo exportado de COMSOL
    
    b1 : objeto de clase Radiofrecuencia
        Campos generados por la simulacion en COMSOL
    
    magnetizacion: objeto de clase Magnetizacion
        Contiene la magnetizacio, la cual se modifica mediante pulsos. Su valor
        inicial es el equilibrio, es decir, vectores unidad en direccion z.
    
    tp : float
        tiempo de pulso.
        
    Methods
    -------
    set_parametros()
        Método utilizado para extraer los parámetros de la simulación del
        `archivo`, y los carga en el atributo `parametros`.    
    
    set_resultados()
        Método utilizado para extraer los resultados de la simulación del 
        `archivo`, y los carga en el atributo `resultados`.
    """

    
    
    def __init__(self, archivo=None, b1=None, tp=None):
        
        self.b1 = b1        
        self.tp = tp
        self.archivo = archivo
        
        self.N_sitios = 1
        self.fraccion_excitada = 0
        self.nutacion = None
        self.senal = 0
        # el metodo crea objetos.
        # recibe los parametros de entrada. Si b1 y tp estan vacios, entonces
        # extrae los resultados del archivo. Si no le das nigun archivo,
        # crea el objeto magnetizacion con las dimensiones de b1 ingresados.
        if not any([archivo, b1, tp]):
            print("Error! ingresar argumentos al crear el objeto ",
                "Simulacion.\n ej: \n\t",
                "sim = Simulacion(archivo = '~/datos.dat') \n\n",
                "o bien, crear objeto b1 de clase Radiofrecuencia: \n\n\t",
                "sim = Simulacion(b1=b1, tp = 0.420)\n\n")
            raise Exception('Error al crear el objeto simulacion!') 

        elif not any([b1, tp]):
            self.extraer_resultados()
            self.N_sitios = int(self.b1.Bx.shape[0])
        else:
            print("Atencion! No se leyeron los resultados porque se forzo",
                  "el ingreso de 'b1', 'magnetizacion' o 'tp'. ")
            self.magnetizacion = Magnetizacion(self.b1.Bx.shape)            
        #----------------------------------------------------------------------
        
    def extraer_resultados(self):
        """
        Este metodo extrae los resultados del archivo y los guarda en los
        atributos `b1` y ((( algo espacial para X Y ? ))). Ademas inicializa
        el objeto magnetizacion con las dimensiones n x 3: 
        n sitios, 3 componentes. Por otro lado, determina el tp utilizando el
        metodo del histograma (el Bxy con mayor ocurrencias).
        """
        # se usa asi:
        # [X, Y, Z, Bx, By, Bz] = self.extraer_resultados()
        print('leyendo archivo de datos...')
        resultados = np.loadtxt(self.archivo, comments='%', unpack=True)
        # elimino las filas que continenen NaN, para ello debo transponer.
        # luego, transpongo para regresar a su tamano original.
        resultados = resultados.transpose()
        resultados = resultados[~np.isnan(resultados).any(axis=1)]
        resultados = resultados.transpose()
        
        [X, Y, Bx, By, Bz] = resultados
        print("Resultados de '"+self.archivo+"' extraidos con exito.")
        
        # obtengo dim para pasarselos a M. lo transpongo para que sea nx3,
        # donde n es la cantidad de sitios
        dimensiones = np.array([Bx, By, Bz]).T.shape
        
        # creo los objetos campo y magnetizacion que son atributos de la clase
        self.b1 = Radiofrecuencia(Bx, By, Bz)
        self.magnetizacion = Magnetizacion(dimensiones)
        
        # estimo el tiempo de pulso
        self.b1.histograma()
        self.tp = np.pi/2 / self.b1.B90
               
        # el return se usa asi:
        # [X, Y, ...] = self.extraer_resultados()
        return resultados
        #----------------------------------------------------------------------        
        
    def pulso(self):
        """
        Metodo que aplica un pulso de duracion tp.
        La matriz de rotacion esta definida en Radiofrecuencia, y es nx3x3.
        Se realiza un producto punto entre esta y M0 es un vector 3x1.
        La salida es setear el valor de M en el atributo magnetizacion.
        ademas se puede acceder mediante un return.
        """
        R = self.b1.generar_matriz_R(self.tp)
        M0 = self.magnetizacion.M0    
        
        M = np.dot(R,M0)
        self.magnetizacion.set_M(M)
        return M
        #----------------------------------------------------------------------
    
    def adquirir_senal(self):
        """
        Metodo que toma la magnetizacion.M y determina senal S, es decir, 
        el modulo de M en el plano xy. Ademas determina la fase, que es el
        angulo que tiene la magnetizacion total respecto al eje x.
        Por otro lado, devuelve la magnetizacion residual en z.
        """
        # debo transponer para poder desempaquetar (unpack) el array.        
        # Mx,My,Mz = self.magnetizacion.M.transpose()
        
        # creacion del objeto de clase Senal
        senal = Senal(self.magnetizacion)
        S = senal.get_total()
        
        self.senal = senal
        self.fraccion_excitada = S/self.N_sitios

        # return S, fase, Mz
        return S
        #----------------------------------------------------------------------
    
    def sim_nutacion(self, tp_list = 'auto', imprimir=False):
        """
        metodo que simula una nutacion, es decir, varia el tiempo de pulso
        y adquiere la senal. 
        """
        if tp_list=='auto':
            tp_list = np.linspace(0, 4*self.tp, 41)
        else:
            tp_list = np.linspace(tp_list[0], tp_list[1], tp_list[2])
            
        i = 0
        signal = []
        #phase = []
        mz = []
        for tp in tp_list:
            # S: amplitud de la FID. Mz, magnetizacion que no fue excitada.
            self.tp = tp
            self.pulso()
            #S, fase, Mz = self.adquirir_senal()
            S = self.adquirir_senal()
            signal.append(S)
            # phase.append(fase)
            # mz.append(Mz)
            i += 1
            if imprimir:
                print('Amplitud de la FID: ', S)
                print('Magnetizacion no excitada: ', Mz)
                # si el pulso fuera perfecto la senal seria igual a la cantidad
                # de sitios.
                self.fraccion_excitada = S/self.N_sitios
                print('fracción excitada: ', self.fraccion_excitada*100, ' %')
                print('-------------------')
            
        signal = np.array(signal)
        # phase = np.array(phase)
        # mz = np.array(mz)
        
        # Creo objeto nutacion: interpola y devuelve tp para pulso de 90
        nutacion = Nutacion(tp_list, signal)
        tp90 = nutacion.get_tp90()
        
        self.tp = tp90
        self.nutacion = nutacion
        return nutacion
        #----------------------------------------------------------------------
        
    def get_b1(self):        
        return self.b1
        #----------------------------------------------------------------------
    
    def get_tp(self):
        return self.tp
        #----------------------------------------------------------------------