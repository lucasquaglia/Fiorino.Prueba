class Empresa(object):
    listaAutos = []
    listaCamionetas = []
    def __init__(self):
        listaAutos = []
        listaCamionetas = []
    def agregarAuto(self,auto):
        self.listaAutos.append(auto)
    def agregarCamioneta(self, camioneta):
        self.listaCamionetas.append()

class Vehiculo(object):

    Patente = ""
    cantidadRuedas = 0
    añoFabricacion = 0
    def sets(self,patente,cantidadR, año):
        self.Patente = patente
        self.cantidadRuedas = cantidadR
        self.añoFabricacion = año

class Camioneta(Vehiculo):

    capacidadCarga = 0
    def __init__(self):
        Vehiculo.cantidadRuedas = 4
    def setCapacidad(self,capacidad):
        self.capacidadCarga = capacidad

class Auto(Vehiculo):

    descapotable = False
    def __init__(self):
        Vehiculo.cantidadRuedas = 4
    def setDescapotable(self,descap):
        self.descapotable = descap