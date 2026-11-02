class Libro:

    def __init__(self, codigo, titulo, autor, anio, categoria, codigo_socio=None):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.categoria = categoria
        self.codigo_socio = codigo_socio

    def esta_libre(self):
        return self.codigo_socio is None

    def prestar(self, codigo_socio):
        self.codigo_socio = codigo_socio

    def devolver(self):
        self.codigo_socio = None
