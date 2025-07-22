# modelos/cita.py

class Cita:
    def __init__(self, id_paciente, id_medico, fecha_hora, motivo_consulta, estado='Programada'):
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.fecha_hora = fecha_hora  # Formato: 'YYYY-MM-DD HH:MM:SS'
        self.motivo_consulta = motivo_consulta
        self.estado = estado
