from estudiante import Estudiante


def subMenuAlumno(estudiante, cursos):
    while True:
        print("\nSub Menu Alumno:")
        print("1. Matricularse a un curso")
        print("2. Ver cursos matriculados")
        print("3. Volver al menú principal")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            print("Lista de Cursos Disponibles:")
            for i in range(len(cursos)):
                print(f"{i+1} {cursos[i]._Curso__nombre}")
            estudiante.matricularEnCurso(cursos)

        elif opcion == "2":
            if len(estudiante._Estudiante__cursos) == 0:
                print("No estas matriculado en ningun curso.")
            else:
                print("Cursos Matriculados:")
                for i in range(len(estudiante._Estudiante__cursos)):
                    curso = estudiante._Estudiante__cursos[i]
                    print(f"{i + 1} {curso._Curso__nombre}")
        elif opcion == "3":
            break
        else:
            print("Opción invalida.")
