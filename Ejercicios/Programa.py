from Clases.curling import *
from datetime import date

Jug1 = Jugador()
Jug1.setNombre("Santiago Fiorino")
Jug1.setNumero(10)

Jug2 = Jugador()
Jug3 = Jugador()
Jug4 = Jugador()
Jug5 = Jugador()

Jug6 = Jugador()
Jug1.setNombre("Jesus")
Jug1.setNumero(10)

Jug7 = Jugador()
Jug8 = Jugador()
Jug9 = Jugador()
Jug10 = Jugador()

#----------------------------------------------------------------------------------------------------------------------

TNP = [False,False,False] #Ese Dia no pueden
TM = [True,False,False] #Turno Mañana
TT = [False,True,False] #Turno Tarde
TN = [False,False,True] #Turno Noche
TMT = [True,True,False] #Turno Mañana y Tarde
TMN = [True,False,True] #Turno Mañana y Noche
TTN = [False,True,True] #Turno Tarde y Noche
TMTN = [True,True,True] #Turno Mañana, Tarde y Noche

#----------------------------------------------------------------------------------------------------------------------

Equipo1 = Equipo()
Equipo1.setCapitan(10)
Equipo1.setNombre("San Lorenzo")

Equipo1.setDisponibilidad(TM) #Lunes
Equipo1.setDisponibilidad(TMT) #Martes
Equipo1.setDisponibilidad(TN) #Miercoles
Equipo1.setDisponibilidad(TMT) #Jueves
Equipo1.setDisponibilidad(TTN) #Viernes
Equipo1.setDisponibilidad(TMTN) #Sabado
Equipo1.setDisponibilidad(TNP) #Domingo

Equipo1.agregarJugador(Jug1) #Agrego Jugadores
Equipo1.agregarJugador(Jug2)
Equipo1.agregarJugador(Jug3)
Equipo1.agregarJugador(Jug4)
Equipo1.agregarJugador(Jug5)

#----------------------------------------------------------------------------------------------------------------------

Equipo2 = Equipo()

Equipo2.setNombre("Boca")
Equipo2.setCapitan(10)

Equipo2.setDisponibilidad(TT) #Lunes
Equipo2.setDisponibilidad(TNP) #Martes
Equipo2.setDisponibilidad(TM) #Miercoles
Equipo2.setDisponibilidad(TMN) #Jueves
Equipo2.setDisponibilidad(TTN) #Viernes
Equipo2.setDisponibilidad(TMN) #Sabado
Equipo2.setDisponibilidad(TNP) #Domingo

Equipo2.agregarJugador(Jug6) #Agrego Jugadores
Equipo2.agregarJugador(Jug7)
Equipo2.agregarJugador(Jug8)
Equipo2.agregarJugador(Jug9)
Equipo2.agregarJugador(Jug10)

#----------------------------------------------------------------------------------------------------------------------

megalolCup = Torneo()

megalolCup.agregarEquipo(Equipo1)
megalolCup.agregarEquipo(Equipo2)

#----------------------------------------------------------------------------------------------------------------------

totalTeam = 0

for team in megalolCup.Equipos:
    totalTeam+=1

numero = 1
totalPartidos = 0

for numero in range (totalTeam):
    totalPartidos+=numero
    numero +=1

numero = 0

for numero in range (totalPartidos):

