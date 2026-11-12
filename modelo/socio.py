class Socio:

    def __init__(self, codigo, nombre, email, codigo_libro=None):
        self.codigo = codigo
        self.nombre = nombre
        self.email = email
        self.codigo_libro = codigo_libro

    def tiene_libro(self):
        return self.codigo_libro is not None

    def coger_libro(self, codigo_libro):
        self.codigo_libro = codigo_libro

    def dejar_libro(self):
        self.codigo_libro = None
