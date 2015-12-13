# -*- coding: utf-8 -*-
class Vehiculo(object):

    """Clase vehículo de mensajeria.
    El coche tiene asignada una ruta y tiene un
    límite de combustible el cual debe aprovechar
    al máximo para recorrer la ruta realizando el
    menor número de paradas durante el trayecto"""

    def __init__(self, gas=0, ruta=None):
        self.gas = gas
        self.ruta = ruta

        print "Datos del coche."
        print "Tanque de combustible del vehículo: " + str(self.gas)

    def set_ruta(self, ruta):
        self.ruta = ruta

    def get_gas(self):
        return self.gas

    def get_ruta(self):
        return self.ruta
