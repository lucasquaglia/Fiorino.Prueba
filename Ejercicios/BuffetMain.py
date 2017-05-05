from Clases610.Buffet import *

Poli = Colegio()
alumnoAux = Alumno()
profeAux = Profesor()
platoAux = Plato()
pedidoAux = Pedido()

while 1:
    print("1) Agregar Alumno")
    print("2) Agregar Profesor")
    print("3) Agregar Plato")
    print("4) Agregar Pedido")
    print("-----------------------")
    print("5) Eliminar Alumno")
    dato = int(input())
    if dato == 1:
        alumnoAux = Alumno()
        print("Nombre:")
        alumnoAux.Nombre = input()
        print("Apellido:")
        alumnoAux.Apellido = input()
        print("Division:")
        alumnoAux.Division = input()
        print("DNI: ")
        alumnoAux.DNI = input()
        Poli.listaPersonas.append(AlumnoAux)
    elif dato == 2:
        profeAux = Profesor()
        print("Nombre:")
        profeAux.Nombre = input()
        print("Apellido:")
        profeAux.Apellido = input()
        print("Descuento:")
        profeAux.Descuento = input()
        print("DNI: ")
        profeAux.DNI = input()
        Poli.listaPersonas.append(profeAux)
    elif dato == 3:
        platoAux = Plato()
        print("Nombre:")
        platoAux.Nombre = input()
        print("Precio:")
        platoAux.Precio = input()
        Poli.listaPlatos.append(platoAux)
    elif dato == 4:
        pedidoAux = Pedido()
        print("Fecha de Entrega:")
        pedidoAux.fechaEntrega = input()
        print("DNI del Comprador:")
        dni = input()
        for person in Poli.listaPersonas:
            if person.DNI == dni:
                pedidoAux.Comprador = person
                break
        print("Hora:")
        pedidoAux.horaEntrega = input()
        print("Plato:")
        plato = input()
        for platos in Poli.listaPlatos:
            if platos.Nombre == plato:
                pedidoAux.Plato = platos
        pedidoAux.seEntrego = False
    elif dato == 5:
        print("DNI de Alumno:")
        dni = input()
        for person in Poli.listaPersonas:
            if person.DNI == dni:
                Poli.eliminarAlumno(person)
                break