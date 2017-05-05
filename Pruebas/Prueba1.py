class Persona(object):
    Nombre = ""
    Apellido = ""
    fechaNac = ""
    Registros = []

    def __init__(self):
        Registros = []

    def setNombre(self,nombre):
        self.Nombre = nombre

    def setApellido(self, apellido):
        self.Apellido = apellido

    def setNacimiento(self,fechaN):
        self.fechaNac = fechaN

    def agregarRegistro(self,registro):
        self.Registros.append(registro)

    def promedios(self,año):
        sumaPeso = 0
        sumaAltura = 0
        i = 0
        for registro in self.Registros:
            if int(registro.fechaReg[0:4]) == año:
                sumaPeso += registro.Peso
                sumaAltura += registro.Altura
                i += 1
        return sumaPeso/i , sumaAltura/i

    def porcentajeCrecimiento(self,año):

        for registro in self.Registros:
            if int(registro.fechaReg[0:4]) == año:
                alturaInicial = registro.Altura
                break
        i = 0
        for registro in self.Registros:
            i += 1
            if int(registro.fechaReg[0:4]) + 1 == año:
                break
        alturaFinal = self.Registros[i-1].Altura
        return (alturaFinal-alturaInicial * 100)/alturaInicial

class Registro(object):
    Peso = 0
    Altura = 0
    fechaReg = ""

    def setPeso(self,peso):
        self.Peso = peso

    def setAltura(self,altura):
        self.Altura = altura

    def setFecha(self,fecha):
        self.fechaReg = fecha
