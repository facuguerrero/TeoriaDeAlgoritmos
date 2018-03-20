# -*- coding: utf-8 -*-

import random

TEST_FILE = "files/test.txt"

class CreadorArchivos(object):
    """
    Crea un archivo con un grafo de n vertices y 2n aristas, conexo
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
        archivo.write(str(2*n) + "\n") #Cantidad de aristas
        self.agregarAristas(n, archivo)

        archivo.close()

    def agregarAristas(self, n, archivo):
        #El grafo debe ser conexo asi que en la primer iteración se
        #recorren todos los vertices y se verifica que no quede ninguno sin unir
        visitados = [i for i in xrange(n)]
        vertPrev = 0
        a = 0
        aristas = dict( (v, []) for v in xrange(n))
        for v in xrange(n):
            if (not v in visitados): continue
            if (len(visitados) == 0): break
            arista = []
            #Se une al vertice random anterior con el actual elegido por orden
            if (a != 0): #debe haber al menos una arista
                aristas[v].append(vertPrev)
                aristas[vertPrev].append(v)
                linea = " ".join([str(vertPrev), str(v)])
                archivo.write(linea + "\n")
            #Se lo saca de visitados y se lo añade a la arista
            visitados.remove(v);
            arista.append(str(v)) #Vertice actual
            #Si ya no quedan vertices, se lo une a cualquiera
            if (len(visitados) == 0):
                dest = random.randint(0, n-1)
            else:
                #Sino, se lo une a un vertice cualquiera del grafo
                dest = random.choice(visitados)
                vertPrev = dest #Para unirlo luego al proximo vertice
                #Se lo saca de visitados y se lo añade a la arista
                visitados.remove(dest);
            arista.append(str(dest)) #Vertice siguiente
            #Se guarda la arista en el vertice
            aristas[v].append(dest)
            aristas[dest].append(v)

            linea = " ".join(arista)
            a += 1
            archivo.write(linea + "\n")

        #Ahora se completan las 2n aristas con cualquier union entre vertices
        #que no exista todavia
        for i in xrange(2*n - a - 2):
            #Vertice de origen
            src = random.randint(0, n-1)
            #Se verifica que no este unido a todos los vertices del grafo
            while (len(aristas[src]) == n): src = random.randint(0, n-1)
            #Vertice de destino
            dest = random.randint(0, n-1)
            #Se verifica si no estan unidos todavia
            while (src in aristas[dest]): dest = random.randint(0, n-1)
            #Se guarda la arista en cada vertice
            aristas[src].append(dest)
            if (src != dest): aristas[dest].append(src)
            #Se escribe la arista
            arista = [str(src), str(dest)]
            linea = " ".join(arista)
            archivo.write(linea + "\n")
