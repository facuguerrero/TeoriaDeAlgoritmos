import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lectorArchivos import LectorArchivos

from floydWarshall import floydWarshall
import time
import math

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


    for i in xrange(len(archivos)):

        print "-----------------------------------------"

        src = raw_input("Vertice origen: ")
        dest = raw_input("Vertice destino: ")

        print "Leyendo archivo " + str(i+1) + "..."

        grafo = lector.initGrafo(archivos[i])

        fw= floydWarshall(grafo)

        n = vertices[i]
        print "Calculando camino minimo en grafo con " + str(n) + " vertices y " + str(n*(n-1)) + " aristas..."
        init = time.time()
        fw.floydWarshall()
        peso, intermedios= fw.calculoDeCaminoMinimo(src,dest)
        end = time.time()

        print "Tiempo transcurrido: " + str(end-init) + "s."

        print "El camino minimo entre " + src + " y " + dest + " tiene un peso de " + str(peso) + " pasando por: \n"
        cam = src
        cam += " "
        for vertex in intermedios:
            cam += vertex
            cam += " "
        cam+= dest
        print cam


def modificarPesos(grafo):
    for vertice in grafo.vertices.keys():
        #Para cada arista en E[G]
        verticesAdyacentes = grafo.obtener_conocidos(vertice) #Vecinos de vertex
        for adyacente in verticesAdyacentes:
            peso = float(grafo.obtener_peso(vertice, adyacente))
            grafo.vertices[vertice][adyacente] = str(-math.log(float(peso)))


main()
