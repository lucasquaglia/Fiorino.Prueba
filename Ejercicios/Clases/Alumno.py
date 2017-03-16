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
        menor = notas[0]
        for nota in notas
            if(nota < menor)
                menor = nota
        return menor

    def setMayor(self):
        mayor = notas[0]
        for nota in notas
            if(nota > mayor)
                mayor = nota
        return mayor

    def setPromedio(self):
        suma = 0
        cantidad = 0
        for nota in notas:
            suma = suma + nota
            cantidad += 1

        return suma/cantidad



