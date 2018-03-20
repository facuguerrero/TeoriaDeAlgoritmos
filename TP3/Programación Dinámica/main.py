# -*- coding: utf-8 -*-

from algoritmoDinamico import SolucionDinamica

def main():
    valoresPorDia = [12, 16, 10, 13, 4, 10]
    valoresPorDia2 = [2, 3, 4, 1, 4, 5]

    pd = SolucionDinamica(valoresPorDia)

    resultado = pd.getBestDays()

    diaCompra = resultado[0]
    diaVenta = resultado[1]
    ganancia = resultado[2]

    print "La mayor ganancia se obtiene comprando el día " + str(diaCompra) + \
        " y vendiendo el día " + str(diaVenta) + " con un valor de " + str(ganancia) + "."

main()
