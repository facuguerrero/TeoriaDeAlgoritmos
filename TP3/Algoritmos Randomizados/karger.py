# -*- coding: utf-8 -*-

from graph import Graph
import copy
import random

class Karger():
    """
        Algoritmo randomizado de Karger para hallar cortes mínimos de un
        grafo conexo no dirigido.
    """
    def __init__(self, graph):
        self.graph = graph


    def contract(self, graph, t):
        """
            Realiza la contracción del grafo hasta que tenga t vertices
        """
        #Se hace una copia del grafo original para modificarlo
        contractedGraph = copy.deepcopy(graph)

        #Se eliminan las aristas que unen a un vertice con él mismo
        contractedGraph.removeSelfEdges()
        #Se itera hasta que queden solo dos vertices
        while (len(contractedGraph) > 2):
            #Se elige una arista al azar
            randomEdge = random.choice(contractedGraph.getEdges())
            #Se obtienen los vertices que componen esa arista
            couple = contractedGraph.getEdge(randomEdge)
            #Se elimina la arista elegida al azar
            contractedGraph.removeEdge(randomEdge)
            #Se unen los vertices de la anterior arista. En caso de que alguna
            #arista resultante sea una selfEdge, es eliminada automaticamente
            contractedGraph.joinVertices(couple[0], couple[1])

        return contractedGraph

    def fastMinCut(self, graph):
        """
            Algoritmo de Karger-Stein para hallar un corte minimo
        """
        n = len(graph)
        #Mientras tenga mas de 8 vertices se utiliza este metodo
        if n > 8:
            #Fast min cut de un grafo contraido hasta [n/sqrt(2) + 1] vertices
            cGraph1 = self.fastMinCut(self.contract(graph, n/(2**0.5) + 1))
            cGraph2 = self.fastMinCut(self.contract(graph, n/(2**0.5) + 1))
            if (len(cGraph1) < len(cGraph2)): return cGraph1
            else: return cGraph2
        #Si son menos de 8, se utiliza la fuerza bruta
        else:
            return self.contract(graph, 2)


    def findMinimumCut(self):
        """
            Devuelve una lista con las aristas que componen el corte mínimo
            del grafo.
        """
        contractedGraph = self.fastMinCut(self.graph)

        #Se obtienen las aristas que quedaron al final de la iteracion
        survivingEdges = contractedGraph.getEdges()
        minimumCut = []
        #A partir de las aristas obtenidas del grafo modificado, se obtienen las
        #aristas del grafo original, que representan el corte minimo
        for survivingEdge in survivingEdges:
            edge = self.graph.getEdge(survivingEdge)
            minimumCut.append( [edge[0], edge[1]] )

        return minimumCut
