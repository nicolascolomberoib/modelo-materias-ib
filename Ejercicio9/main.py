from clases import Persona, Estudiante, Materia, Admin

def main():
    # Crear estudiantes
    est1 = Estudiante("Ana Pérez", 20, "Ingeniería Nuclear")
    est2 = Estudiante("Luis Gómez", 22, "Física")
    est3 = Estudiante("María López", 19, "Vocacional")

    # Crear docentes
    docente1 = Persona("Dr. Ricardo Sánchez", 50)
    docente2 = Persona("Dra. Laura Fernández", 45)

    # Crear una materia
    materia = Materia("Física Moderna", 2025)

    # Agregar estudiantes y docentes
    materia.agrega_estudiante(est1)
    materia.agrega_estudiante(est2)
    materia.agrega_estudiante(est3)
    materia.agrega_docente(docente1)
    materia.agrega_docente(docente2)

    # Imprimir estudiantes
    Admin.imprimir_estudiantes(materia)

    # Registrar notas
    materia.registrar_nota(est1, 9)
    materia.registrar_nota(est2, 8)
    materia.registrar_nota(est3, 7)

    # Generar certificados
    Admin.expedir_certificado(materia, est1)
    Admin.expedir_certificado(materia, est2)
    Admin.expedir_certificado(materia, est3)

if __name__ == "__main__":
    main()
