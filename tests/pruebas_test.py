# tests/pruebas_test.py

import unittest
from modelos.medico import Medico
from modelos.paciente import Paciente
from modelos.cita import Cita

class TestClasesBasicas(unittest.TestCase):

    def test_medico_creado_correctamente(self):
        medico = Medico("Luis", "Fernández", "Cardiología", "9991234567", "lfernandez@hospital.com")
        self.assertEqual(medico.nombre, "Luis")
        self.assertEqual(medico.especialidad, "Cardiología")

    def test_paciente_creado_correctamente(self):
        paciente = Paciente("Ana", "López", "1995-08-14", "Femenino", "Calle 45", "9998887766", "ana@example.com")
        self.assertEqual(paciente.genero, "Femenino")
        self.assertIn("1995", paciente.fecha_nacimiento)

    def test_cita_creada_correctamente(self):
        cita = Cita(1, 2, "2025-07-25 15:00:00", "Chequeo general")
        self.assertEqual(cita.id_medico, 2)
        self.assertEqual(cita.estado, "Programada")

if __name__ == '__main__':
    unittest.main()
