# db/controlador_db.py
from db.db_config import obtener_conexion

def insertar_medico(medico):
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
            INSERT INTO Medicos (nombre, apellido, especialidad, telefono_profesional, email_profesional)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(consulta, (
                medico.nombre,
                medico.apellido,
                medico.especialidad,
                medico.telefono_profesional,
                medico.email_profesional
            ))
            conexion.commit()
            print("Médico registrado correctamente.")
        except Exception as e:
            print("Error al insertar médico:", e)
        finally:
            cursor.close()
            conexion.close()

from db.db_config import obtener_conexion

def insertar_paciente(paciente):
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
            INSERT INTO Pacientes (nombre, apellido, fecha_nacimiento, genero, direccion, telefono, email)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(consulta, (
                paciente.nombre,
                paciente.apellido,
                paciente.fecha_nacimiento,
                paciente.genero,
                paciente.direccion,
                paciente.telefono,
                paciente.email
            ))
            conexion.commit()
            print("Paciente registrado correctamente.")
        except Exception as e:
            print("Error al insertar paciente:", e)
        finally:
            cursor.close()
            conexion.close()

def insertar_cita(cita):
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
            INSERT INTO Citas (id_paciente, id_medico, fecha_hora, motivo_consulta, estado)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(consulta, (
                cita.id_paciente,
                cita.id_medico,
                cita.fecha_hora,
                cita.motivo_consulta,
                cita.estado
            ))
            conexion.commit()
            print("Cita registrada correctamente.")
        except Exception as e:
            print("Error al insertar cita:", e)
        finally:
            cursor.close()
            conexion.close()

def obtener_historial_citas(id_paciente):
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)  # Esto permite devolver resultados como diccionario
            consulta = """
            SELECT Citas.id_cita, Citas.fecha_hora, Citas.motivo_consulta, Citas.estado,
                   Medicos.nombre AS nombre_medico, Medicos.apellido AS apellido_medico
            FROM Citas
            JOIN Medicos ON Citas.id_medico = Medicos.id_medico
            WHERE Citas.id_paciente = %s
            ORDER BY Citas.fecha_hora DESC;
            """
            cursor.execute(consulta, (id_paciente,))
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print("Error al obtener historial de citas:", e)
            return []
        finally:
            cursor.close()
            conexion.close()

def cancelar_cita(id_cita):
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "UPDATE Citas SET estado = 'Cancelada' WHERE id_cita = %s"
            cursor.execute(consulta, (id_cita,))
            conexion.commit()
            if cursor.rowcount > 0:
                print(f"Cita ID {id_cita} cancelada correctamente.")
            else:
                print(f"No se encontró la cita ID {id_cita}.")
        except Exception as e:
            print("Error al cancelar la cita:", e)
        finally:
            cursor.close()
            conexion.close()

def reprogramar_cita(id_cita, nueva_fecha_hora):
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
                UPDATE Citas
                SET fecha_hora = %s, estado = 'Reprogramada'
                WHERE id_cita = %s
            """
            cursor.execute(consulta, (nueva_fecha_hora, id_cita))
            conexion.commit()
            if cursor.rowcount > 0:
                print(f"Cita ID {id_cita} reprogramada para {nueva_fecha_hora}.")
            else:
                print(f"No se encontró la cita ID {id_cita}.")
        except Exception as e:
            print("Error al reprogramar la cita:", e)
        finally:
            cursor.close()
            conexion.close()

def insertar_cita(cita):
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
            INSERT INTO Citas (id_paciente, id_medico, fecha_hora, motivo_consulta, estado)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(consulta, (
                cita.id_paciente,
                cita.id_medico,
                cita.fecha_hora,
                cita.motivo_consulta,
                cita.estado
            ))
            conexion.commit()
            print("Cita registrada correctamente.")
        except Exception as e:
            print("Error al insertar cita:", e)
        finally:
            cursor.close()
            conexion.close()

def obtener_medicos():
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id_medico, nombre, apellido FROM Medicos")
            return cursor.fetchall()
        except:
            return []

def obtener_pacientes():
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id_paciente, nombre, apellido FROM Pacientes")
            return cursor.fetchall()
        except:
            return []
