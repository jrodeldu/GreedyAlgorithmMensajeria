 # -*- coding: utf-8 -*-
class Ruta(object):

    """La ruta tiene como propiedades
    el número de paradas que componen la misma
    y las distancias de una a la otra"""

    nparadas = 0
    listaparadas = None

    def __init__(self, data):
        mydata 				= data[:]
        self.nparadas 		= len(mydata)
        self.listaparadas 	= data

    def get_listaparadas(self):
        return self.listaparadas
