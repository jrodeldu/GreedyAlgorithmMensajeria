 # -*- coding: utf-8 -*-


class Greedy(object):

    """Clase que contiene el algoritmo voraz
    adaptado al proyecto de mensajería.
    Se deben realizar el menor número de paradas
    posibles durante el recorrido de la ruta"""

    solution = None
    candidates = None

    def __init__(self, vehiculo, ioMensajeria):
        self.vehiculo        = vehiculo
        self.ioMensajeria   = ioMensajeria
        self.candidates        = vehiculo.get_ruta().get_listaparadas()

        #print "Greedy data."
        #print self.vehiculo.get_gas()
        #print self.vehiculo.get_ruta().get_listaparadas()

        self.ioMensajeria.log("Greedy data.")
        self.ioMensajeria.log("Autonomía del vehículo en Kms: " + str(self.vehiculo.get_gas()))
        self.ioMensajeria.log("Lista de distancias entre paradas: " + str(self.vehiculo.get_ruta().get_listaparadas()))

    def execute(self):
        capacidad_gas = self.vehiculo.get_gas()
        paradas_totales = len(self.candidates)
        kms_recorridos = 0
        i = 0
        print "="*75
        print "Capacidad gasolina: " + str(capacidad_gas)
        print "Kms recorridos: " + str(kms_recorridos)
        print "Paradas posibles desde origen: " + str(paradas_totales)
        while i < paradas_totales - 1:
            while kms_recorridos <= capacidad_gas and i < paradas_totales - 1:
                print "Llegando a la parada (" + str(i+1) + ") a " + self.candidates[i] + " Kms distancia"
                kms_recorridos += float(self.candidates[i])
                i += 1
            if kms_recorridos > capacidad_gas:
                print "Recorridos " + str(kms_recorridos - float(self.candidates[i-1])) + " Kms"
                print "============== Hay que parar en la parada " + str(i-1) + " =============="
                kms_recorridos = 0
                i -= 1
            if i == paradas_totales - 1:
                print "Recorridos " + str(kms_recorridos + float(self.candidates[i])) + " Kms"
                print "============== Llegamos a la parada final " + str(i+1) + " =============="
