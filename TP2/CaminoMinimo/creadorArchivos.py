import random

TEST_FILE = "files/test.txt"
MAX_PESO = 20.00

class CreadorArchivos(object):
    """
    Crea un archivo con n grafos dirijidos completos
    """

    def __init__(self):
        pass

    def crearArchivo(self, n, filePath = TEST_FILE):
        """
        Crea el archivo de prueba.
        Parametros:
            - n {int} Cantidad de vertices
        """

        try:
            archivo = open(filePath, "w")
        except IOError:
            raise ValueError, "Error al abrir el archivo!"

        archivo.write(str(n) + "\n") #Cantidad de vertices
        archivo.write(str(n*(n-1)) + "\n") #Cantidad de aristas
        self.agregarAristas(n, archivo)

        archivo.close()

    def agregarAristas(self, n, archivo):
        cambio = dict( (e, dict( (a, None) for a in xrange(n))) for e in xrange(n))
        for i in xrange(0, n): #Para cada vertice
            for j in xrange(0, n): #Se agregan las n-1 aristas
                arista = []
                if j == i: continue #No esta unido consigo mismo
                arista.append(str(i)) #Vertice actual
                arista.append(str(j)) #Vertice siguiente
                peso = cambio[i][j]
                if peso is None:
                    nuevoPeso = random.uniform(0.05, MAX_PESO)
                    extraSpice = random.uniform(-0.005, 0.005) #cuarto decimal
                    if (random.randint(1, 10) > 5):
                        cambio[i][j] = nuevoPeso
                        cambio[j][i] = 1.0/nuevoPeso + extraSpice
                        peso = nuevoPeso
                    else:
                        cambio[j][i] = nuevoPeso
                        cambio[i][j] = 1.0/nuevoPeso + extraSpice
                        peso = 1.0/nuevoPeso + extraSpice
                arista.append(str(int(peso*1000)/1000.0)) #Peso
                linea = " ".join(arista)
                archivo.write(linea + "\n")
