 # -*- coding: utf-8 -*-


class Greedy(object):

    """Clase que contiene el algoritmo voraz
    adaptado al proyecto de mensajería.
    Se deben realizar el menor número de paradas
    posibles durante el recorrido de la ruta"""

    solucion = []
    candidatos = None

    def __init__(self, vehiculo, ioMensajeria):
        self.vehiculo        = vehiculo
        self.ioMensajeria    = ioMensajeria
        self.candidatos      = vehiculo.get_ruta().get_listaparadas()

        #print "Greedy data."
        #print self.vehiculo.get_gas()
        #print self.vehiculo.get_ruta().get_listaparadas()

    def execute(self):
        capacidad_gas = self.vehiculo.get_gas()
        paradas_totales = len(self.candidatos)
        kms_recorridos = 0
        i = 0
        self.ioMensajeria.log("="*75)
        self.ioMensajeria.log("Capacidad gasolina: " + str(capacidad_gas))
        self.ioMensajeria.log("Kms recorridos: " + str(kms_recorridos))
        self.ioMensajeria.log("Paradas posibles desde origen: " + str(paradas_totales))
        self.ioMensajeria.log("Lista de distancias entre paradas:\n" + str(self.candidatos))
        while i < paradas_totales - 1:
            while kms_recorridos <= capacidad_gas and i < paradas_totales - 1:
                kms_recorridos += float(self.candidatos[i])
                i += 1
            if kms_recorridos > capacidad_gas:
                kms_recorridos -= float(self.candidatos[i-1])
                # Hay que repostar en la parada previa para poder llegar a la siguiente
                self.solucion.append([i-1, kms_recorridos])
                kms_recorridos = 0
                i -= 1
            if i == paradas_totales - 1:
                kms_recorridos += float(self.candidatos[i])
                # Llegada al final
                self.solucion.append([i+1, kms_recorridos])
        # Imprimir solución
        self.ioMensajeria.log("Partiendo desde origen (parada 0) se realizan los siguientes repostajes:")
        for index, parada in enumerate(self.solucion, 1):
            if index == len(self.solucion):
                msg = "Llegada al final de la ruta habiendo recorrido " + str(parada[1]) + " Kms"
            else:
                msg = "Repostaje en parada " + str(parada[0]) + " habiendo recorrido " + str(parada[1]) + " Kms"
            self.ioMensajeria.log(msg)
