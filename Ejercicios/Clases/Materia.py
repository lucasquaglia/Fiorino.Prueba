class Materiaa (object)

    nombre = ""
    notas = []

    def setNombre(self,a):
        self.nombre=a

    def setNotas(self,b):
        (self.notas).append(b)

    def setPromedioNotas(self):
        return sum(self.notas)/len(self.notas)


