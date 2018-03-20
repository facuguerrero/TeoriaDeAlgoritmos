from graph import Graph

TEST_FILE = "files/test.txt"

class LectorArchivos(object):
    """
    Se encarga de abrir y leer los archivos de prueba, crea un grafo a partir de los datos leidos.
    """

    def __init__(self):
        pass

    def initGrafo(self, filePath = TEST_FILE):
        """
        Crea el grafo para la prueba a partir del archivo que esta en el path indicado.
            - filePath {string} Direccion del archivo.
        El archivo debe ser del tipo: (#k, numero de linea k)
            #1 - |V|
            #2 - |E|
            #3...#n - Vi Vj <--- Vertices que estan unidos, indicados por numeros separados
                                por un espacio
        """
        grafo = Graph()

        try:
            archivo = open(filePath, "r")
        except IOError:
            raise ValueError, "Error al abrir archivo!"

        lineas = archivo.readlines() #Lista con todas las lineas del archivo
        archivo.close()

        #Las primeras dos lineas son |V| y |E| y no se usan asi que se omiten
        lineas = lineas[2:]
        aristas = 0 #Contador de aristas, numero que se usa como key de cada arista
        for linea in lineas:
            vertices = linea.split(' ') #Se obtienen los vertices
            vertices[1] = vertices[1][:len(vertices[1])-1] #Se saca el \n del segundo vertice
            grafo.addEdge(aristas, int(vertices[0]), int(vertices[1])) #Se agrega la arista
            aristas += 1

        return grafo
