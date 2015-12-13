# -*- coding: utf-8 -*-
import iomensajeria.iomensajeria as io
from mensajero import buildermensajeria as builder
from greedy.greedy import *
class Mensajeria(object):

    """
    Clase principal del programa.
    Se pide un fichero de salida y uno de entrada para poder
    ejecutar el algoritmo.
    El fichero de salida puede ser ninguno, por lo que en else
    caso la salida de log será a través de la consola.
    El fichero de entrada debe se válido a los requisitos del
    problema, de lo contrario la aplicación llegará a su fin.
    """

    fin             = None
    fout            = None
    ioMensajeria    = None
    data            = None

    def __init__(self, fin=None, fout=None):
        """Inicializar la aplicación"""

        self.fin 	= fin
        self.fout 	= fout

        # Definir entrada y salida
        self.__define_output()
        self.__define_input()

    def __define_output(self):
        if not self.fout:
            while True:
                self.fout = raw_input("Introduzca un nombre del fichero de salida, de lo contrario la salida será por pantalla: > ")
                try:
                    if not self.fout:
                        # Salida por consola
                        self.fout = 0
                    else:
                        with open(self.fout, 'w') as data:
                            # Fichero de salida creado
                            data.write("Fichero de salida creado.")
                            data.write("\n")
                    break
                except IOError as IOerr:
                    print "Nombre de fichero incorrecto: " + str(IOerr)

    def __define_input(self):
        if not self.fin:
            while True:
                self.fin = raw_input("Introduzca un nombre del fichero de entrada: > ")
                break
        #else:
        self.__open_fin()

    def __open_fin(self):
        self.ioMensajeria = io.IOMensajeria(self.fin, self.fout)
        if not self.ioMensajeria.get_error():
            # Una vez obtenido un fichero válido ya tenemos datos para procesar
            self.data = self.ioMensajeria.get_data()
        else:
            print "No hay datos disponibles. Fin de la aplicación"
            print "*" * 50 + "\n"

    def build_app(self):
        """Una vez definidos la entrada y salida del programa se
        procede a construir la aplicación y ejecutar el algoritmo"""
        myBuild = builder.BuilderMensajeria(self, self.ioMensajeria)
        self.greedy = Greedy(myBuild.get_vehiculo(), self.ioMensajeria)

    def set_fin(self, f):
        self.fin = f

    def set_fout(self, f):
        self.fout = f

    def get_data(self):
        return self.data

if __name__ == "__main__":
    a = Mensajeria()
    a.build_app()
