# interfaz/interfaz_gui.py

import tkinter as tk
from tkinter import messagebox
from modelos.medico import Medico
from modelos.paciente import Paciente
from db.controlador_db import insertar_medico, insertar_paciente
from modelos.cita import Cita
from db.controlador_db import insertar_cita, obtener_medicos, obtener_pacientes
from tkinter import ttk
from db.controlador_db import insertar_cita, obtener_medicos, obtener_pacientes, obtener_historial_citas
from db.controlador_db import cancelar_cita, reprogramar_cita

class AplicacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión Médica")
        self.root.geometry("500x500")

        # Frame dinámico donde se cargarán los formularios
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        self.crear_menu()
        self.mostrar_formulario_medico()  # Por defecto

    def crear_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        registro_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Registrar", menu=registro_menu)
        registro_menu.add_command(label="Médico", command=self.mostrar_formulario_medico)
        registro_menu.add_command(label="Paciente", command=self.mostrar_formulario_paciente)
        registro_menu.add_command(label="Cita", command=self.mostrar_formulario_cita)
        consultar_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Consultar", menu=consultar_menu)
        consultar_menu.add_command(label="Historial de Citas", command=self.mostrar_historial_paciente)
        menubar.add_command(label="Modificar Cita", command=self.mostrar_modificar_cita)





    def limpiar_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def mostrar_formulario_medico(self):
        self.limpiar_frame()

        tk.Label(self.main_frame, text="Registro de Médico", font=("Helvetica", 16)).pack(pady=10)

        self.medico_nombre = self.crear_entry("Nombre")
        self.medico_apellido = self.crear_entry("Apellido")
        self.medico_especialidad = self.crear_entry("Especialidad")
        self.medico_telefono = self.crear_entry("Teléfono profesional")
        self.medico_email = self.crear_entry("Email profesional")

        tk.Button(self.main_frame, text="Registrar Médico", command=self.registrar_medico).pack(pady=10)

    def mostrar_formulario_paciente(self):
        self.limpiar_frame()

        tk.Label(self.main_frame, text="Registro de Paciente", font=("Helvetica", 16)).pack(pady=10)

        self.pac_nombre = self.crear_entry("Nombre")
        self.pac_apellido = self.crear_entry("Apellido")
        self.pac_fecha_nac = self.crear_entry("Fecha de nacimiento (YYYY-MM-DD)")
        self.pac_genero = self.crear_entry("Género")
        self.pac_direccion = self.crear_entry("Dirección")
        self.pac_telefono = self.crear_entry("Teléfono")
        self.pac_email = self.crear_entry("Email")

        tk.Button(self.main_frame, text="Registrar Paciente", command=self.registrar_paciente).pack(pady=10)

    def crear_entry(self, etiqueta):
        tk.Label(self.main_frame, text=etiqueta).pack()
        entrada = tk.Entry(self.main_frame)
        entrada.pack()
        return entrada

    def registrar_medico(self):
        medico = Medico(
            nombre=self.medico_nombre.get(),
            apellido=self.medico_apellido.get(),
            especialidad=self.medico_especialidad.get(),
            telefono_profesional=self.medico_telefono.get(),
            email_profesional=self.medico_email.get()
        )

        try:
            insertar_medico(medico)
            messagebox.showinfo("Éxito", "Médico registrado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar el médico:\n{e}")

    def registrar_paciente(self):
        paciente = Paciente(
            nombre=self.pac_nombre.get(),
            apellido=self.pac_apellido.get(),
            fecha_nacimiento=self.pac_fecha_nac.get(),
            genero=self.pac_genero.get(),
            direccion=self.pac_direccion.get(),
            telefono=self.pac_telefono.get(),
            email=self.pac_email.get()
        )

        try:
            insertar_paciente(paciente)
            messagebox.showinfo("Éxito", "Paciente registrado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar el paciente:\n{e}")

    def mostrar_formulario_cita(self):
        self.limpiar_frame()

        tk.Label(self.main_frame, text="Registro de Cita Médica", font=("Helvetica", 16)).pack(pady=10)

        # Pacientes
        tk.Label(self.main_frame, text="Paciente").pack()
        self.pacientes_lista = obtener_pacientes()
        self.pacientes_combo = ttk.Combobox(self.main_frame, values=[
            f"{p[0]} - {p[1]} {p[2]}" for p in self.pacientes_lista
        ])
        self.pacientes_combo.pack()

        # Médicos
        tk.Label(self.main_frame, text="Médico").pack()
        self.medicos_lista = obtener_medicos()
        self.medicos_combo = ttk.Combobox(self.main_frame, values=[
        f"{m[0]} - {m[1]} {m[2]}" for m in self.medicos_lista
        ])
        self.medicos_combo.pack()

        # Fecha y motivo
        self.fecha_cita = self.crear_entry("Fecha y hora (YYYY-MM-DD HH:MM:SS)")
        self.motivo = self.crear_entry("Motivo de la consulta")

        tk.Button(self.main_frame, text="Registrar Cita", command=self.registrar_cita).pack(pady=10)

    def registrar_cita(self):
        try:
            id_paciente = int(self.pacientes_combo.get().split(" - ")[0])
            id_medico = int(self.medicos_combo.get().split(" - ")[0])
            fecha_hora = self.fecha_cita.get()
            motivo = self.motivo.get()

            cita = Cita(
                id_paciente=id_paciente,
                id_medico=id_medico,
                fecha_hora=fecha_hora,
                motivo_consulta=motivo
            )

            insertar_cita(cita)
            messagebox.showinfo("Éxito", "Cita registrada correctamente")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar la cita:\n{e}")

    def mostrar_historial_paciente(self):
        self.limpiar_frame()

        tk.Label(self.main_frame, text="Consultar Historial de Citas", font=("Helvetica", 16)).pack(pady=10)

        # Selector de paciente
        tk.Label(self.main_frame, text="Selecciona un paciente").pack()
        pacientes = obtener_pacientes()
        self.historial_combo = ttk.Combobox(self.main_frame, values=[
            f"{p[0]} - {p[1]} {p[2]}" for p in pacientes
        ])
        self.historial_combo.pack()

        tk.Button(self.main_frame, text="Ver historial", command=self.cargar_historial).pack(pady=10)

        self.resultado_historial = tk.Text(self.main_frame, height=15, width=60)
        self.resultado_historial.pack(pady=10)
    
    def cargar_historial(self):
        try:
            id_paciente = int(self.historial_combo.get().split(" - ")[0])
            citas = obtener_historial_citas(id_paciente)

            self.resultado_historial.delete("1.0", tk.END)

            if not citas:
                self.resultado_historial.insert(tk.END, "No se encontraron citas para este paciente.")
                return

            for cita in citas:
                info = (
                    f"Fecha: {cita['fecha_hora']}\n"
                    f"Médico: {cita['nombre_medico']} {cita['apellido_medico']}\n"
                    f"Motivo: {cita['motivo_consulta']}\n"
                    f"Estado: {cita['estado']}\n"
                "-----------------------------\n"
                )
                self.resultado_historial.insert(tk.END, info)

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener el historial:\n{e}")

    def mostrar_modificar_cita(self):
        self.limpiar_frame()

        tk.Label(self.main_frame, text="Modificar o Cancelar Cita", font=("Helvetica", 16)).pack(pady=10)

        # Selector de paciente
        tk.Label(self.main_frame, text="Selecciona un paciente").pack()
        self.pacientes_mod = obtener_pacientes()
        self.combo_pac_mod = ttk.Combobox(self.main_frame, values=[
            f"{p[0]} - {p[1]} {p[2]}" for p in self.pacientes_mod
        ])
        self.combo_pac_mod.pack()

        tk.Button(self.main_frame, text="Cargar citas", command=self.cargar_citas_paciente).pack(pady=10)

        self.combo_citas = ttk.Combobox(self.main_frame)
        self.combo_citas.pack(pady=5)

        self.nueva_fecha = self.crear_entry("Nueva fecha (YYYY-MM-DD HH:MM:SS)")

        tk.Button(self.main_frame, text="Reprogramar", command=self.reprogramar_cita_gui).pack(pady=5)
        tk.Button(self.main_frame, text="Cancelar cita", command=self.cancelar_cita_gui).pack(pady=5)

    def cargar_citas_paciente(self):
        try:
            id_paciente = int(self.combo_pac_mod.get().split(" - ")[0])
            citas = obtener_historial_citas(id_paciente)
            self.citas_dict = {f"{c['id_cita']} - {c['fecha_hora']} - {c['estado']}": c['id_cita'] for c in citas}
            self.combo_citas['values'] = list(self.citas_dict.keys())
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar citas:\n{e}")

    def cancelar_cita_gui(self):
        try:
            texto = self.combo_citas.get()
            id_cita = self.citas_dict[texto]
            cancelar_cita(id_cita)
            messagebox.showinfo("Éxito", f"Cita ID {id_cita} cancelada.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cancelar:\n{e}")

    def reprogramar_cita_gui(self):
        try:
            texto = self.combo_citas.get()
            id_cita = self.citas_dict[texto]
            nueva_fecha = self.nueva_fecha.get()
            reprogramar_cita(id_cita, nueva_fecha)
            messagebox.showinfo("Éxito", f"Cita ID {id_cita} reprogramada.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo reprogramar:\n{e}")




