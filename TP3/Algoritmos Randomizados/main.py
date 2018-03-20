# -*- coding: utf-8 -*-

from creadorArchivos import CreadorArchivos
from lectorArchivos import LectorArchivos
from graph import Graph
from karger import Karger

def main():
    #Se crean los archivos
    print "Creando archivo..."
    creador = CreadorArchivos()
    #creador.crearArchivo(100)
    #Se lee un archivo y se crea el grafo
    print "Leyendo grafo..."
    lector = LectorArchivos()
    grafo = lector.initGrafo()

    #Se crea el objeto que resuelve el problema
    karger = Karger(grafo)
    #Se resuelve el problema
    print "Ejecutando el algoritmo de Karger-Stein [(ln(100)^2)] veces en un grafo G = (100, 200)... \t"
    bestMinCut = [0]*100
    for i in xrange(22):
        minCut = karger.findMinimumCut()
        if len(minCut) < len(bestMinCut): bestMinCut = minCut
    print "El corte más pequeño obtenido tiene " + str(len(bestMinCut)) + " aristas. Las cuales son:"
    for edge in bestMinCut:
        print edge

main()
