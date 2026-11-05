from modelo.libro import Libro


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


def main():
    print("Sistema de gestión de biblioteca")
    libros = cargar_libros()
    print("Libros cargados:", len(libros))


main()
