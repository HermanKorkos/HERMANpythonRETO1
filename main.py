from modelo.libro import Libro
from modelo.socio import Socio


def cargar_libros():
    libros = []
    fichero = open("libros.txt", "r", encoding="utf-8")
    for linea in fichero:
        linea = linea.strip()
        if linea == "":
            continue
        partes = linea.split(";")
        codigo_socio = partes[5]
        if codigo_socio == "":
            codigo_socio = None
        libro = Libro(partes[0], partes[1], partes[2], int(partes[3]), partes[4], codigo_socio)
        libros.append(libro)
    fichero.close()
    return libros


def cargar_socios():
    socios = []
    fichero = open("socios.txt", "r", encoding="utf-8")
    for linea in fichero:
        linea = linea.strip()
        if linea == "":
            continue
        partes = linea.split(";")
        codigo_libro = partes[3]
        if codigo_libro == "":
            codigo_libro = None
        socio = Socio(partes[0], partes[1], partes[2], codigo_libro)
        socios.append(socio)
    fichero.close()
    return socios


def main():
    print("Sistema de gestión de biblioteca")
    libros = cargar_libros()
    socios = cargar_socios()
    print("Se han cargado", len(libros), "libros y", len(socios), "socios")


main()
