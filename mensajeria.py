# -*- coding: utf-8 -*-
import sys
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
    fout            = True
    ioMensajeria    = None
    data            = None
    myBuild         = None

    def __init__(self, fin=None, fout=True):
        """Inicializar la aplicación"""
        self.fin 	= fin
        self.fout 	= fout

    def init(self):
        self.define_in_out()
        #self.build_app()
        try:
            #self.__open_fin()
            self.build_app()
        except TypeError as err:
            template = "An exception of type {0} occured. Arguments:\n{1!r}"
            message = template.format(type(err).__name__, err.args)
            print message
	
    def restart(self):
        self.fin            = None
        self.fout           = True
        self.ioMensajeria   = None
        self.data           = None
        self.myBuild        = None
        self.fin 			= None
        while True:
            input = raw_input("Desea reiniciar la aplicación? (y/n)")
            if input in ('y', 'n'):
                if input == 'y':
                    self.init()
                    break
                else:
                    sys.exit()
                
	
    def define_in_out(self):
        # Definir entrada y salida
        self.define_output()
        self.define_input()

    def define_output(self):
        if self.fout:
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

    def define_input(self):
        if not self.fin:
            while True:
                self.fin = raw_input("Introduzca un nombre del fichero de entrada: > ")
                if self.fin:
                    break
        self.data = self.__open_fin()

    def __open_fin(self):
        self.ioMensajeria = io.IOMensajeria(self.fin, self.fout)
        # Una vez obtenido un fichero válido ya tenemos datos para procesar
        data = self.ioMensajeria.get_data()
        return data

    def build_app(self):
        """Una vez definidos la entrada y salida del programa se
        procede a construir la aplicación y ejecutar el algoritmo"""
        self.myBuild = builder.BuilderMensajeria(self.data, self.ioMensajeria)
        vehiculo = self.myBuild.get_vehiculo()
        if vehiculo is not None:
            myGreedy = Greedy(self.myBuild.get_vehiculo(), self.ioMensajeria)
            myGreedy.execute()
        else:
            #raise TypeError("El vehículo no ha sido creado debido a un error con los datos de entrada")
            self.data = None

    def set_fin(self, f):
        self.fin = f

    def set_fout(self, f):
        self.fout = f

    def get_data(self):
        return self.data

if __name__ == "__main__":
    a = Mensajeria()
    a.init()
	
