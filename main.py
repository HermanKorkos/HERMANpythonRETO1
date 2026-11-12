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


def recortar(texto, largo):
    if len(texto) > largo:
        return texto[:largo - 3] + "..."
    return texto


def mostrar_libros(lista):
    print()
    print(f"{'CÓDIGO':<7}{'TÍTULO':<38}{'AUTOR':<26}{'AÑO':>5}  {'CATEGORÍA':<17}ESTADO")
    print("-" * 106)
    for libro in lista:
        if libro.esta_libre():
            estado = "Libre"
        else:
            estado = "Prestado a " + libro.codigo_socio
        titulo = recortar(libro.titulo, 36)
        autor = recortar(libro.autor, 24)
        print(f"{libro.codigo:<7}{titulo:<38}{autor:<26}{libro.anio:>5}  {libro.categoria:<17}{estado}")
    print("Total:", len(lista), "libros")


def listar_todos(libros):
    mostrar_libros(libros)


def listar_disponibles(libros):
    disponibles = []
    for libro in libros:
        if libro.esta_libre():
            disponibles.append(libro)
    mostrar_libros(disponibles)


def mostrar_menu():
    print()
    print("--- BIBLIOTECA ---")
    print("1. Ver todos los libros")
    print("2. Ver libros disponibles")
    print("3. Buscar libro por título")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Socios con libro")
    print("7. Añadir socio o libro")
    print("8. Salir")


def main():
    print("Sistema de gestión de biblioteca")
    libros = cargar_libros()
    socios = cargar_socios()
    print("Se han cargado", len(libros), "libros y", len(socios), "socios")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "8":
            print("Hasta luego")
            break
        elif opcion == "1":
            listar_todos(libros)
        elif opcion == "2":
            listar_disponibles(libros)
        elif opcion in ["3", "4", "5", "6", "7"]:
            print("Opción todavía no disponible")
        else:
            print("Opción no válida, elige un número del 1 al 8")


main()
