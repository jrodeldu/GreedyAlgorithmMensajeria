# -*- coding: utf-8 -*-

# import sys
# from os import path
# Recuperamos ruta absoluta del fichero y subimos al directorio principal
# sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
# Una vez en el directorio principal importamos
# from mensajero import buildermensajeria

class IOMensajeria(object):

    """Clase IO para el proyecto de mensajeria.
    La funcionalidad de esta clase es proporcionar
    una forma sencilla de leer y escribir ficheros
    de entrada y salida.
    Ofrece posibilidad de que la salida sea a través
    de la consola"""

    foutput = None
    data    = None

    def __init__(self, filein, foutput=None):
        """
        Inicializamos la instancia definiendo salida estandar.
        Si foutput es None la salida será la consola
        Si foutput no es None la salida será el fichero
        """
        self.foutput = foutput
        try:
            with open(filein) as f:
                # Obtenemos una lista con los valores del fichero
                # sin '\n' al final de cada elemento
                self.data = f.read().splitlines()
                # print self.data
                self.log("Datos de entrada: " + str(self.data))
        except IOError as err:
			template = "An exception of type {0} occured. Arguments:\n{1!r}"
			message = template.format(type(err).__name__, err.args)
			print message            
			print "*" * 50 + "\n"

    def log(self, mensaje):
        """Grabamos mensaje de log en la salida definida"""
        if not self.foutput:
            print(mensaje)
        else:
            try:
                with open(self.foutput, 'a') as data:
                    data.write(str(mensaje))
                    data.write("\n")
            except IOError as err:
                print err

    def get_data(self):
        return self.data
