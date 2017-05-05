class Jugador(object):

    Nombre = ""
    fechaNac = None
    Numero = 0

    def setNombre(self, nombre):
        self.Nombre = nombre

    def setfechaNac(self,fecha):
        self.fechaNac = fecha

    def setNumero(self,numero):
        self.Numero = numero

class Equipo(object):

    Nombre = ""
    Barrio = ""
    Capitan = 0
    Disponibilidad = []
    listaJugadores = []

    def __init__(self):
        self.Disponibilidad = []
        self.listaJugadores = []

    def agregarJugador(self, jugador):
        for jugActual in self.listaJugadores:
            if jugActual.Numero == jugador.Numero:
                return False
        (self.listaJugadores).append(jugador)

    def setDisponibilidad(self, turno): #Turno es el array de 3 (Mañana, tarde o noche)
        (self.Disponibilidad).append(turno)

    def setNombre(self, nombre):
        self.Nombre = nombre

    def setCapitan(self,numero):
        self.Capitan = numero

    def setBarrio(self, barrio):
        self.Barrio = barrio

class Partido(object):

    Dia = None
    Turno = ""
    Equipos = []

    def __init__(self):
        self.Equipos = []

    def setDia(self, dia):
        self.Dia = dia

    def setTurno(self, turno):
        self.Turno = turno

    def setEquipos(self,equipo):
        (self.Equipos).append(equipo)

class Torneo(object):

    Equipos = []
    listaPartidos = []

    def __init__(self):
        self.Equipos = []
        self.listaPartidos = []

    def agregarEquipo(self,equipo):
        for equipoActual in self.listaPartidos:
            if equipoActual.Nombre == equipo.Nombre:
                return False
        (self.Equipos).append(equipo)

    def agregarPartido(self,partido):
        (self.listaPartidos).append(partido)


