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
    print("5) Eliminar Persona")
    print("6) Modificar Persona")
    print("-----------------------")
    print("7) Guardar")

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
        Poli.listaPersonas.append(alumnoAux)
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
        print("DNI:")
        dni = input()
        for person in Poli.listaPersonas:
            if person.DNI == dni:
                Poli.eliminarPersona(person)
                break
    elif dato == 6:
        print("DNI:")
        dni = input()
        for person in Poli.listaPersonas:
            if person.DNI == dni:
                print("1) Modificar Nombre")
                print("2) Modificar Apellido")
                print("3) Modificar Descuento")
                dato2 = int(input())
                if dato2 == 1:
                    print("Nombre:")
                    person.Nombre = input()
                elif dato2 == 2:
                    print("Apellido:")
                    person.Apellido = input()
                elif dato2 == 3:
                    if person.getDescuento() == 0:
                        print("Un alumno no puede tener descuento")
                        input()
                        break
                    else:
                        print("Descuento: ")
                        desc = input()
                        person.Descuento = desc
    elif dato == 7:
        Poli.guardar()
