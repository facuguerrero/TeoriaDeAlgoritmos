from creadorArchivos import CreadorArchivos
from lectorArchivos import LectorArchivos

FILE_1 = "files/g1.txt"
FILE_2 = "files/g2.txt"
FILE_3 = "files/g3.txt"
FILE_4 = "files/g4.txt"
FILE_5 = "files/g5.txt"
FILE_6 = "files/g6.txt"
FILE_7 = "files/g7.txt"
FILE_8 = "files/g8.txt"
FILE_9 = "files/g9.txt"
FILE_10 = "files/g10.txt"
FILE_11 = "files/g11.txt"
FILE_12 = "files/g12.txt"

def main():
    creador = CreadorArchivos()

    creador.crearArchivo(10, FILE_1);
    creador.crearArchivo(50, FILE_2);
    creador.crearArchivo(100, FILE_3);
    creador.crearArchivo(350, FILE_4);
    creador.crearArchivo(500, FILE_5);
    creador.crearArchivo(750, FILE_6);
    creador.crearArchivo(1000, FILE_7);
    creador.crearArchivo(1250, FILE_8);
    creador.crearArchivo(1500, FILE_9);
    creador.crearArchivo(1750, FILE_10);
    creador.crearArchivo(2000, FILE_11);
    creador.crearArchivo(2500, FILE_12);

main();
