class LectorArchivos(object):
    """
    Se encarga de abrir y leer los archivos de prueba, crea una lista a partir de los datos leidos.
    """

    def __init__(self):
        pass

    def initLista(self, filePath):
        """
        Crea la lista para la prueba a partir del archivo que esta en el path indicado.
            - filePath {string} Direccion del archivo.
        El archivo debe ser del tipo: (#k, numero de linea k)
            #1 - target
            #2...#n - numeros enteros positivos
        """
        list = []

        try:
            archivo = open(filePath, "r")
        except IOError:
            raise ValueError, "Error al abrir archivo!"

        lineas = archivo.readlines() #Lista con todas las lineas del archivo
        archivo.close()

        t = (lineas[0].split(' '))[0]
        lineas = lineas[1:] #se saltea t
        for linea in lineas:
            num = linea.split(' ') #Se obtiene el numero
            list.append(int(num[0])) #el segundo elemento es \n

        return list, int(t)
