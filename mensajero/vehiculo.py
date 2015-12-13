# -*- coding: utf-8 -*-
class Vehiculo(object):

    """Clase veh�culo de mensajeria.
    El coche tiene asignada una ruta y tiene un
    l�mite de combustible el cual debe aprovechar
    al m�ximo para recorrer la ruta realizando el
    menor n�mero de paradas durante el trayecto"""

    def __init__(self, gas=0, ruta=None):
        self.gas = gas
        self.ruta = ruta

        print "Datos del coche."
        print "Tanque de combustible del veh�culo: " + str(self.gas)

    def set_ruta(self, ruta):
        self.ruta = ruta

    def get_gas(self):
        return self.gas

    def get_ruta(self):
        return self.ruta
