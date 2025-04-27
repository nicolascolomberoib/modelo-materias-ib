
from utilidades import numero_a_letras
import os

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    CARRERAS_VALIDAS = [
        'Ingeniería Nuclear', 
        'Ingeniería Mecánica', 
        'Ingeniería en Telecomunicaciones', 
        'Física', 
        'Vocacional'
    ]

    def __init__(self, nombre, edad, carrera):
        if carrera not in self.CARRERAS_VALIDAS:
            raise ValueError(f"Carrera inválida: {carrera}. Las válidas son: {', '.join(self.CARRERAS_VALIDAS)}")
        super().__init__(nombre, edad)
        self.carrera = carrera

    def presentarse(self):
        return f"{super().presentarse()} Estoy estudiando {self.carrera}."

class Materia:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio
        self.estudiantes = []
        self.docentes = []
        self.notas = {}

    def agrega_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def agrega_docente(self, docente):
        self.docentes.append(docente)

    def imprime_estudiantes(self):
        print(f"Estudiantes de la materia {self.nombre} ({self.anio}):")
        for estudiante in self.estudiantes:
            print(estudiante.presentarse())

    def registrar_nota(self, estudiante, nota):
        if estudiante not in self.estudiantes:
            raise ValueError(f"El estudiante {estudiante.nombre} no está inscripto en {self.nombre}.")
        self.notas[estudiante] = nota

class Admin:
    @staticmethod
    def imprimir_estudiantes(materia):
        materia.imprime_estudiantes()

    @staticmethod
    def expedir_certificado(materia, estudiante, carpeta_destino="certificados"):
        if estudiante not in materia.estudiantes:
            raise ValueError(f"{estudiante.nombre} no está inscripto en {materia.nombre}.")

        nota = materia.notas.get(estudiante)
        if nota is None:
            raise ValueError(f"No se registró nota para {estudiante.nombre}.")

        nota_letras = numero_a_letras(nota)

        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        nombre_archivo = f"{carpeta_destino}/certificado_{estudiante.nombre.replace(' ', '_')}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(f"Certificado de Aprobación\n")
            f.write(f"Nombre del estudiante: {estudiante.nombre}\n")
            f.write(f"Materia: {materia.nombre} ({materia.anio})\n")
            f.write(f"Nota: {nota} ({nota_letras})\n")

        print(f"Certificado generado para {estudiante.nombre}: {nombre_archivo}")
