# modelos/paciente.py

class Paciente:
    def __init__(self, nombre, apellido, fecha_nacimiento, genero, direccion, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento  # Formato: 'YYYY-MM-DD'
        self.genero = genero
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
