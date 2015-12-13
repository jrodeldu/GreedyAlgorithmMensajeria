 # -*- coding: utf-8 -*-

from vehiculo import *
from ruta import *

class BuilderMensajeria(object):

    """Clase Builder que creará el objeto
    vehículo y ruta asinada al mismo si
    no se detecta ningún error durante
    el checkeo previo de distancias entre
    paradas"""

    mensajeria 		= None
    ioMmensajeria 	= None
    data			= None

    def __init__(self, mensajeria, ioMensajeria=None):
        """
        Se construyen los elementos requeridos por la
        aplicación controlando los posibles errores
        que pueda provocar la información del fichero
        de entrada respecto a capacidad y distancias
        """

        # Datos proporcionados por fichero
        self.data       	= mensajeria.get_data()
        print self.data
        print mensajeria.data
        print mensajeria.get_data()
        self.ioMensajeria 	= ioMensajeria

        try:
            # Crear ruta
            self.build_ruta()
            # Crear vehívulo
            self.build_vehiculo()
            # Asignar rutal al vehículo
            self.vehiculo.set_ruta(self.ruta)
        except (ValueError, AttributeError) as err:
            print "Error: " + str(err)
            print "Fin de la aplicación."
            print "*" * 50 + "\n"
            self.mensajeria.start()

    def build_vehiculo(self):
        """
        Crear vehículo comprobando el valor numérico de su tanque de combustible
        """
        gas = float(self.data[0])
        self.vehiculo = Vehiculo(gas)

    def build_ruta(self):
        """
        Crear la ruta.
        Comprobar que los valores de las distancias son numéricos
        Comprobar que ninguna distancia es superior a la
        autonomía del vehículo
        Comprobar que el número de distancias es igual a self.data[1] - 1
        p.ej. si el segundo número del fichero es 10 debe de haber 9 distancias,
        el origen es la parada 0
        """
        nparadas     = int(self.data[1]) - 1     # Valor de num paradas - 1
        distancias   = self.data[2:]             # Copia de distancias

        if not nparadas == len(distancias):
            raise AttributeError("El número de distancias de la ruta es %i y debería ser %i" % (len(distancias), nparadas))

        print "GAS: " + str(self.data[0])
        for d in distancias:
            print d
            float(d)
            if float(d) > float(self.data[0]):
                err = str(d) + " es menor que " + str(self.data[0])
                raise AttributeError("Hay distancias mayores a la autonomía disponible del vehículo: " + err)
        self.ruta = Ruta(distancias)

    def get_ruta():
        return self.ruta

    def get_vehiculo(self):
        return self.vehiculo

    def get_mensajeria():
        return self.mensajeria

    def get_ioMensajeria(self):
        return self.ioMensajeria
