from datetime import date

class Colegio(object):
    listaPersonas = []
    listaPedidos = []
    listaPlatos = []
    def __init__(self):
        self.listaPersonas = []
        self.listaPedidos = []
        self.listaPlatos = []
    def agregarPersona(self,persona):
        self.listaPersonas.append(persona)
    def agregarPedido(self,pedido):
        self.listaPedidos.append(pedido)
    def agregarPlato(self,plato):
        self.listaPlatos.append(plato)
    def pedidosDelDia(self):
        pedidiosDeHoy = []
        for pedido in self.listaPedidos:
            if pedido.fechaEntrega == datetime.now:
                pedidiosDeHoy.append(pedido)
        return pedidiosDeHoy
    def eliminarPersona(self,personita):
        for person in listaPersonas:
            if person == personita:
                listaPersonas.remove(personita)
                break
    def guardar(self):
        f = open("archivo.txt","w")
        for persona in self.listaPersonas:
            f.write("1" + "|" +persona.Nombre + "|" + persona.Apellido           #1 porque es un alumno
                    + "|" + persona.DNI + "|" + str(persona.getDescuento()) + '\n')
        for plato in self.listaPlatos:
            f.write("2" + "|" + plato.Nombre + "|" + plato.Precio)       #2 porque es un plato
        f.close()
class Persona(object):
    Nombre = ""
    Apellido = ""
    DNI = 0
    def setNombre(self,nombre):
        self.Nombre = nombre
    def setApelido(self,apellido):
        self.Apellido = apellido
    def getDescuento(self):
        return 0
class Alumno(Persona):
    Division = ""
    def setDivision(self,division):
        self.Division = division
class Profesor(Persona):
    Descuento = 0
    def setDescuento(self,descuento):
        self.Descuento = descuento
    def getDescuento(self):
        return  self.Descuento
class Plato(object):
    Nombre = ""
    Precio = 0
    def setNombre(self,nombre):
        self.Nombre = nombre
    def setPrecio(self,precio):
        self.Precio = precio
class Pedido(object):
    fechaEntrega = None
    Comprador = None
    horaEntrega = ""
    Plato = None
    seEntrego = False
    def setFechaC(self,fecha):
        self.fechaEntrega = fecha
    def setComprador(self,persona):
        self.Comprador = persona
    def setHoraEntrega(self,hora):
        self.horaEntrega = hora
    def setPlato(self,plato):
        self.Plato = plato
    def entrega(self,bool):
        self.seEntrego = bool