
class AproxSubsetSum(object):
    """
    Aprox SubsetSum para subconjuntos enteros positivos, y un t entero positivo
    """

    def __init__(self, subset, t, sigma):
        """
        :param subset: lista de enteros positivos
        :param t: entero positivo
        :param sigma: parametro de aproximacion entre 0 y 1
        """
        self.subset = subset
        self.target = t
        self.sigma = sigma

    def getAproxSubsetSum(self):
        """
        Calcula el valor aproximado de SubsetSum donde el resultado
        esta a un factor de (1 + sigma) de la solucion optima
        :return: entero positivo
        """
        n = len(self.subset)
        listaAnterior = []
        listaAnterior.append(0)

        for i in xrange(0, n):
            listaActual = self.mergeLists(listaAnterior, self.subset[i])
            listaTrim = self.trim(listaActual, (self.sigma / (2*n)))
            self.cleanList(listaTrim)
            listaAnterior = listaTrim

        return listaAnterior[len(listaAnterior) - 1]



############ Funciones auxiliares ##############


    def trim(self, subset, delta):
        """
        Se remueven del subset la mayor cantidad de elementos
         posibles, dependiendo de delta(factor de cortado)
        :param delta: numero positivo entre 0 y 1
        :param subset: subconjunto de enteros positivos ordenados crecientemente
        :return: nuevo subconjuto recortado del original por el factor delta
        """
        newSubset = []
        newSubset.append(subset[0])
        anterior = subset[0]

        for i in xrange(1,len(subset)):
            actual = subset[i]

            if (actual > (anterior * (1 + delta))):
                newSubset.append(actual)
                anterior = actual

        return newSubset


    def mergeLists(self, lista, factor):
        """
        Ordena la lista y le suma el factor a cada uno de sus elementos
        :param listaAnterior: lista de enteros positivos
        :param factor: entero positivo
        :return: nueva Lista ordenada crecientemente y modificada
        """

        if(len(lista) > 1):

            for i in xrange(1, len(lista)):
                valorActual = lista[i]
                lista.append(valorActual + factor)

        lista.append(factor)
        lista.sort()
        return lista

    def cleanList(self, lista):
        """
        elimina todo elemento de la lista que sea mayor que el target
        :param lista: lista de enteros
        """

        listaCopy = list(lista)

        for elem in listaCopy:
            if (elem > self.target):
                lista.remove(elem)
