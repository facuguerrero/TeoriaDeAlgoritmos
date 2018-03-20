import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lectorArchivos import LectorArchivos
from dijkstra import Dijkstra
import time
import math
import random

GRAFO1 = "../files/g1.txt"
GRAFO2 = "../files/g2.txt"
GRAFO3 = "../files/g3.txt"
GRAFO4 = "../files/g4.txt"
GRAFO5 = "../files/g5.txt"
GRAFO6 = "../files/g6.txt"
GRAFO7 = "../files/g7.txt"
GRAFO8 = "../files/g8.txt"
GRAFO9 = "../files/g9.txt"
GRAFO10 = "../files/g10.txt"
GRAFO11 = "../files/g11.txt"
GRAFO12 = "../files/g12.txt"


def main():

    lector = LectorArchivos()
    archivos = [GRAFO1, GRAFO2, GRAFO3, GRAFO4, GRAFO5, GRAFO6, GRAFO7, GRAFO8, GRAFO9, GRAFO10, GRAFO11, GRAFO12]
    vertices = [10, 50, 100, 350, 500, 750, 1000, 1250, 1500, 1750, 2000, 2500]

    i = 1
    for i in xrange(len(archivos)):
        print "-----------------------------------------"
        print "Leyendo archivo " + str(i+1) + "..."
        grafo = lector.initGrafo(archivos[i])
        #modificarPesos(grafo) #Se modifican los pesos para el problema de las finanzas

        D = Dijkstra(grafo)

        #Se eligen aleatoriamente los vertices de destino y de inicio
        n = vertices[i]
        src = str(random.randint(0, n-1))
        dest = str(random.randint(0, n-1))

        while (dest == src): dest = str(random.randint(0, n-1))
        print "Vertice de inicio: " + src + " | Vertice de destino: " + dest

        print "Calculando camino minimo en grafo con " + str(n) + " vertices y " + str(n*(n-1)) + " aristas..."
        init = time.time()
        (path, weight) = D.getShortestPath(int(src), int(dest))
        end = time.time()
        #Se pone el tiempo mas lindo
        delta = end-init;
        hrs = int(delta)/3600
        mins = int(delta-3600*hrs)/60
        secs = delta-3600*hrs-60*mins
        print "Tiempo transcurrido: " + str(hrs) + "h " + str(mins) + "m " + str(secs) + "s."

        print "El camino minimo entre " + src + " y " + dest + " tiene un peso de " + str(weight) + " recorriendo: "
        for vertex in path:
            print vertex,
        print "\n"

main()
