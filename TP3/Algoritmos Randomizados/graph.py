# -*- coding: utf-8 -*-

import heapq
INFINITO = 2000000000.0

class Graph():
    """
        Grafo no dirigido sin pesos.
    """

    def __init__(self):
        self.edges = {} #Diccionario de aristas
        self.vertices = {} #Diccionario de vertices
        self.size = 0 #Cantidad de vertices

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.edges)

    def getEdges(self):
        return self.edges.keys()

    def addEdge(self, key, u, v):
        #Se agrega la arista
        self.edges[key] = [u, v]
        #Se agrega a cada vertice la arista, y si no existe el vertice, se lo agrega al grafo
        #Vertice u
        if self.vertices.has_key(u):
            self.vertices[u].append(key)
        else:
            self.vertices[u] = [key]
            self.size += 1
        #Si es una arista de u en u, se agrega una sola vez
        if u == v: return
        #Vertice v
        if self.vertices.has_key(v):
            self.vertices[v].append(key)
        else:
            self.vertices[v] = [key]
            self.size += 1

    def getEdge(self, key):
        return self.edges[key]

    def joinVertices(self, u, v):
        #A todas las aristas que contienen u, se les cambia u por v
        for edge in self.vertices[u]:
            couple = self.edges[edge]
            #Se reemplaza el vertice u con el v en todas las que aparezca u
            if couple[0] == u: couple[0] = v
            if couple[1] == u: couple[1] = v
            #Se se formo una arista de v con v, se elimina
            if couple[0] == couple[1]:
                del self.edges[edge] #Se borra de las aristas
                self.vertices[v].remove(edge) #Se borra del vertice
            #Se agrega a la lista de aristas de v
            elif couple[0] == v or couple[1] == v: self.vertices[v].append(edge)
        #Se borra el vertice u
        del self.vertices[u]
        self.size -= 1

    def removeSelfEdges(self):
        #Se recorren todas las aristas
        for edge in self.edges.keys():
            couple = self.edges[edge]
            #Si la arista tiene dos vertices iguales, se elimina
            if (couple[0] == couple[1]):
                self.vertices[couple[0]].remove(edge) #Se borra del vertice
                del self.edges[edge] #Se borra de las aristas

    def removeEdge(self, key):
        couple = self.edges[key]
        #Se saca la arista de ambos vertices
        self.vertices[couple[0]].remove(key)
        self.vertices[couple[1]].remove(key)
        #Se elimina la arista
        del self.edges[key]
