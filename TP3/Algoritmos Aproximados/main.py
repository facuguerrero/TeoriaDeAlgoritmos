import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from LectorArchivos import LectorArchivos
from AproxSubsetSum import AproxSubsetSum
import time
import random

LIST1 = "files/g1.txt"
LIST2 = "files/g2.txt"
LIST3 = "files/g3.txt"
LIST4 = "files/g4.txt"
LIST5 = "files/g5.txt"
LIST6 = "files/g6.txt"
LIST7 = "files/g7.txt"
LIST8 = "files/g8.txt"
LIST9 = "files/g9.txt"
LIST10 = "files/g10.txt"
LIST11 = "files/g11.txt"
LIST12 = "files/g12.txt"


def main():

    lector = LectorArchivos()
    archivos = [LIST1, LIST2, LIST3, LIST4, LIST5, LIST6, LIST7, LIST8, LIST9, LIST10, LIST11, LIST12]

    sigma = random.random() #devuelve un 0<=sigma<1
    if sigma == 0.0: sigma = 0.5 #caso de que sigma sea cero


    for i in xrange(len(archivos)):
        print "-----------------------------------------"
        print "Leyendo archivo " + str(i+1) + "..."
        lista, t = lector.initLista(archivos[i])

        Sum = AproxSubsetSum(lista, t, sigma)

        print "Cantidad de numeros n: " + str(len(lista)) + " | Target t: " + str(t) + " | Sigma: " + str(sigma)

        print "Calculando AproxSubsetSum"
        init = time.time()
        z = Sum.getAproxSubsetSum()
        end = time.time()
        #Se pone el tiempo mas lindo
        delta = end-init;
        hrs = int(delta)/3600
        mins = int(delta-3600*hrs)/60
        secs = delta-3600*hrs-60*mins
        print "Tiempo transcurrido: " + str(hrs) + "h " + str(mins) + "m " + str(secs) + "s."

        print "La mayor suma de elementos con resultado menor o igual a " + str(t) + " tiene un valor de: " + str(z)

main()
