# Sistema de gestión de biblioteca

Proyecto final de Python de la 1ª evaluación. Es un programa de consola para llevar los libros y los socios de una biblioteca, hecho con clases, funciones y ficheros txt.

## Cómo ejecutarlo

Hace falta Python 3. Desde la carpeta del proyecto

```
python main.py
```

Al arrancar carga los libros y los socios de los ficheros y enseña el menú.

## Estructura

```
modelo/
    libro.py            clase Libro
    socio.py            clase Socio
errores/
    prestamo_error.py   excepción PrestamoError
main.py                 programa principal y menú
libros.txt              100 libros
socios.txt              15 socios
log.txt                 se crea solo al prestar o devolver
```

Cada línea de los txt es un libro o un socio con los campos separados por punto y coma. Si el último campo está vacío el libro está libre o el socio no tiene libro.

## Menú

1. Ver todos los libros
2. Ver los libros disponibles
3. Buscar un libro por cualquier palabra del título
4. Prestar un libro a un socio
5. Devolver el libro que tiene un socio
6. Ver los socios que tienen libro
7. Añadir un socio o un libro
8. Salir y guardar los cambios en los txt

Los préstamos, las devoluciones, los préstamos que fallan y las altas se apuntan en `log.txt` con el formato `[Fecha][evento][detalles]`.

## Posibles mejoras

- Guardar los datos en una base de datos (por ejemplo SQLite) en vez de en ficheros txt.
- Que un socio pueda tener más de un libro a la vez, con un límite.
- Apuntar la fecha del préstamo y avisar de los libros que llevan mucho tiempo sin devolver.
- Poder modificar y borrar libros y socios, no solo añadirlos.
- Comprobar que el email tiene un formato correcto al dar de alta un socio.
- Buscar también por autor o por categoría, y ordenar los listados.
- Paginar el listado de todos los libros para que no salgan los 100 de golpe.
- Guardar los cambios cada vez que se presta o se devuelve, y no solo al salir, para no perder nada si el programa se cierra de golpe.
- Una interfaz gráfica con Tkinter.
- Pruebas automáticas con `unittest` para las clases y los préstamos.

## Ramas

Se ha trabajado en la rama `dev` con una rama `feature/...` para cada parte (estructura, excepción, datos, carga de datos, menú, listados, buscar, préstamos, altas, guardar y log). Al acabar se junta todo en `main` con un pull request.

## Autor

Herman Korkos, 2º DAM
