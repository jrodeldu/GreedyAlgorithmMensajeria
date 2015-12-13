 # -*- coding: utf-8 -*-


class Greedy(object):

    """Clase que contiene el algoritmo voraz
    adaptado al proyecto de mensajería.
    Se deben realizar el menor número de paradas
    posibles durante el recorrido de la ruta"""

    def __init__(self, vehiculo, ioMensajeria):
        self.vehiculo         = vehiculo
        self.ioMensajeria     = ioMensajeria

        print "Greedy data."
        print self.vehiculo.get_gas()
        print self.vehiculo.get_ruta().get_listaparadas()

        self.ioMensajeria.log("Greedy data.")
        self.ioMensajeria.log("Autonomía del vehículo en Kms: " + str(self.vehiculo.get_gas()))
        self.ioMensajeria.log("Lista de distancias entre paradas: " + str(self.vehiculo.get_ruta().get_listaparadas()))

    def execute(self):
        pass
