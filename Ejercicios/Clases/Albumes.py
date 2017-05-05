class Album(object):

    Titulo = ""
    Canciones = []

    def __init__(self):
        self.Canciones = []

    def setTitulo(self, titulo):
        self.Titulo = titulo

    def agregarCancion(self, cancion):
        self.Canciones.append(cancion)

    def devolverArtistas(self):
        listaArtistas = []
        for cancion in self.Canciones:
            for artista in cancion.Artistas:
                if artista not in listaArtistas:
                    listaArtistas.append(artista)
        return listaArtistas

    def artistaInfluyente(self):
        artistas = self.devolverArtistas()
        cantidadCanciones = []
        for artista in artistas:
            cantidadCanciones.append(0)
        for cancion in self.Canciones:
            for artista in cancion.Artistas:
                i = 0;
                for artista2 in artistas:
                    if(artista2==artista):
                        break
                    i+=1
                cantidadCanciones[i]+=1
        maximo = max(cantidadCanciones)
        i=0
        for maxi in cantidadCanciones:
            if maxi==maximo:
                break
            i+=1
        return artistas[i]





class Cancion(object):

    Titulo = ""
    Autores = []
    Artistas = []

    def __init__(self):
        self.Autores = []
        self.Artistas = []

    def setTitulo(self, titulo):
        self.Titulo = titulo

    def agregarArtista(self, artista):
        self.Artistas.append(artista)

    def agregarAutor(self, autor):
        self.Autores.append(autor)

class Persona(object):

    Nombre = ""
    Apellido = ""