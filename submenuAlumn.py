from estudiante import Estudiante

def subMenuAlumno(estudiante, cursos):
    while True:
        print("\nSub Menú Alumno:")
        print("1. Matricularse a un curso")
        print("2. Desmatricularse de un curso")
        print("3. Ver cursos matriculados")
        print("4. Volver al menú principal")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            print("Lista de Cursos Disponibles:")
            for i, curso in enumerate(cursos, 1):
                print(f"{i}. {curso.nombre}")
            
            while True:
                seleccion = input("Ingrese el número del curso al que desea matricularse (o 'cancelar' para volver al menú): ")
                if seleccion.lower() == "cancelar":
                    print("Volviendo al menú principal.")
                    break

                if seleccion.isnumeric():
                    seleccion = int(seleccion)
                    if 1 <= seleccion <= len(cursos):
                        curso_seleccionado = cursos[seleccion - 1]
                        if curso_seleccionado in estudiante._Estudiante__cursos:
                            print("Ya estás matriculado en este curso.")
                        else:
                            print(f"Código de Matriculación: {curso_seleccionado.clave}")
                            clave_matriculacion = input(f"Ingrese la contraseña de matriculación para {curso_seleccionado.nombre}: ")
                            if clave_matriculacion == curso_seleccionado.clave:
                                estudiante._Estudiante__cursos.append(curso_seleccionado)
                                print(f"Te has matriculado en {curso_seleccionado.nombre}.")
                                break
                            else:
                                print("Contraseña incorrecta. No puedes matricularte en el curso.")
                    else:
                        print("Opción inválida.")
                else:
                    print("Opción inválida.")

        elif opcion == "2":
            if len(estudiante._Estudiante__cursos) == 0:
                print("No estás matriculado en ningún curso.")
            else:
                print("Cursos matriculados:")
                for i, curso in enumerate(estudiante._Estudiante__cursos, 1):
                    print(f"{i}. {curso.nombre}")
                while True:
                    seleccion = input("Ingrese el número del curso del que desea desmatricularse (o 'cancelar' para volver al menú): ")
                    if seleccion.lower() == "cancelar":
                        print("Volviendo al menú principal.")
                        break
                    if seleccion.isnumeric():
                        seleccion = int(seleccion)
                        if 1 <= seleccion <= len(estudiante._Estudiante__cursos):
                            curso_seleccionado = estudiante._Estudiante__cursos[seleccion - 1]
                            print(f"Código de Matriculación: {curso_seleccionado.clave}")
                            clave_desmatriculacion = input(f"Ingrese la contraseña de desmatriculación para {curso_seleccionado.nombre}: ")
                            if clave_desmatriculacion == curso_seleccionado.clave:
                                estudiante._Estudiante__cursos.remove(curso_seleccionado)
                                print(f"Te has desmatriculado de {curso_seleccionado.nombre}.")
                                break
                            else:
                                print("Contraseña incorrecta. No puedes desmatricularte del curso.")
                        else:
                            print("Opción inválida.")
                    else:
                        print("Opción inválida.")

        elif opcion == "3":
            print("Cursos matriculados:")
            for i, curso in enumerate(estudiante._Estudiante__cursos, 1):
                print(f"{i}. {curso.nombre}")

        elif opcion == "4":
            print("Volviendo al menú principal.")
            break

        else:
            print("Opción inválida. Por favor, elija una opción válida.")
