class Alumnoo (object):

    nombre = ""
    apellido = ""
    fecha_nac = none
    notas = []

    def setNombre(self,a):
        self.nombre = str(a)

    def setApellido(self,b):
        self.apellido = str(b)

    def setNacimiento(self,c):
        self.fecha_nac = c

    def setNotas(self,d):
        (self.notas).append(d)

    def setMenor(self):
        return min(self.notas)

    def setMayor(self):
        return max(self.notas)

    def setPromedio(self):
        return sum(self.notas)/len(self.notas)