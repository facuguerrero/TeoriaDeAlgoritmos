import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from graph import *


INF  = 1000000000.0

class floydWarshall():

    """Algoritmo de Bellman-Ford para encontrar el camino minimo
    entre todos los pares de vertices de un grafo dirigido
    Camino es un atributo para guardar los vertices para llegar del nodo
    A al nodo B."""
    def __init__(self, grafo):
        self.grafo = grafo
        self.dist = {}
        self.camino = {}
        self.inicializarDiccionarios(grafo)

    def inicializarDiccionarios(self, grafo):
        """Funcion para inicializar copia de los grafos"""
        for vertice in grafo.get_vertices():

            self.dist[vertice] = {}
            self.camino[vertice] = {}
            for adyacente in grafo.get_vertices().get(vertice):

                self.dist[vertice][adyacente] = grafo.get_vertices().get(vertice).get(adyacente)
                self.camino[vertice][adyacente] = []

    """Algoritmo de floydWarshall.
    Luego de terminado el algoritmo el diccionario de distancias debe contener
    las menores distancias entra cada par de vertices.
    Es inicializado como la matriz de adyacencia del grafo dado por parametro."""

    def floydWarshall(self):
        numV = len(self.grafo)

        for k in xrange(numV):
            #aca puede arrancar en 1
            for i in xrange(numV):
                #aca puede arrancar en 2
                for j in xrange(numV):
                    auxK = str(k)
                    auxI = str(i)
                    auxJ = str(j)

                    #inicializamos por primera vez el camino para llegar de un vertice al otro
                    #como la coneccion entre ellos.

                    if(not self.dist[auxI].has_key(auxK) or not self.dist[auxK].has_key(auxJ) or not self.dist[auxI].has_key(auxJ) ):
                        continue

                    distAux = float(self.dist[auxI][auxK]) + float(self.dist[auxK][auxJ])

                    if(float(self.dist[auxI][auxJ]) > distAux ):
                        self.dist[auxI][auxJ] = str(distAux)
                        
                        #Esto no es parte del algoritmo pero se hace para tener la lista de recorridos
                        if(not auxK in self.camino[auxI][auxJ]):
                            self.camino[auxI][auxJ] = [auxK]
                        self.camino[auxI][auxJ] += self.camino[auxK][auxJ]

    def calculoDeCaminoMinimo(self, src, dst):
        return (self.dist[src][dst], self.camino[src][dst])
