import random

TEST_FILE = "files/test.txt"
FACTOR_RANDOM = 10

class CreadorArchivos(object):
    """
    Crea un archivo con n numeros enteros positivos y un t entero positivo
    """

    def __init__(self):
        pass

    def crearArchivo(self, n, filePath = TEST_FILE):
        """
        Crea el archivo de prueba.
        Parametros:
            - n {int} Cantidad de numeros
        """

        try:
            archivo = open(filePath, "w")
        except IOError:
            raise ValueError, "Error al abrir el archivo!"

        t = random.randint(1, FACTOR_RANDOM * n)
        archivo.write(str(t) + " \n") #target t
        self.agregarNumeros(n, archivo)

        archivo.close()

    def agregarNumeros(self, n, archivo):
        for i in xrange(0, n): #n enteros
            num = random.randint(1, FACTOR_RANDOM * n)
            archivo.write(str(num) + " \n")
