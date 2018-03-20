class SolucionDinamica():

    def __init__(self, listaPrediccion):
        self.prediccion = listaPrediccion
        self.tam = len(listaPrediccion)

    def getBestDays(self):
        """
        Idea para no olvidarme.
        Te quedas con el minimo hasta el momento que es dia venta aux.
        entonces vas comparando ganancia entre el dia i y el dia que mas barato
        te salio comprar hasta este momento. Cuando tu ganancia temporal es mas grande
        que la ganancia maxima hasta el momento actualizas esta ultima. En el caso de
        encontrar un dia donde te sale mas barato comprar acciones vos ya sabes
        que hasta el momento no pudiste obtener una ganancia maxima a la que ya tenes,
        entonces actualizas el minimo en dia compra aux y seguis comparando con las posiciones
        que te falten para adelante.
        """

        gananciaMax = 0
        gananciaTemporal = 0
        diaCompra = 0
        diaVenta = 0
        diaCompraAux = 0

        for x in xrange(1, self.tam): #Para todos los dias de la prediccion

            #Este chequeo lo hago antes porque si el valor actual es menor al valor de compra, da negativo
            #Se verifica si hay un dia en que se puede comprar mas barato
            if(self.prediccion[diaCompraAux] > self.prediccion[x]):
                diaCompraAux = x

            #Me quedo con la ganancia del dia que menos sale comprar con el dia actual
            #La ganancia temporal es el precio del dia que compre menos el precio del dia actual
            gananciaTemporal = self.prediccion[x] - self.prediccion[diaCompraAux]

            #Si los valores actuales son mejores que los anteriores, se reemplazan
            if(gananciaMax < gananciaTemporal):
                gananciaMax = gananciaTemporal
                diaCompra = diaCompraAux
                diaVenta = x

        return (diaCompra, diaVenta, gananciaMax)
