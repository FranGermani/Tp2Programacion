from curso import Curso
from archivo import *

def submenuProfesor(profesor, cursos):
    while True:
        print("\nSub Menú Profesor:")
        print("1. Dictar curso")
        print("2. Ver cursos dictados")
        print("3. Volver al menú principal")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            nombre_curso = input("Ingrese el nombre del curso: ")
            carrera_curso = input("Ingrese la carrera del curso: ")
            nuevo_curso = Curso(nombre_curso, carrera_curso)
            cursos.append(nuevo_curso)
            profesor.dictarCurso(nuevo_curso)
            print(f"Curso creado exitosamente:\nNombre: {nuevo_curso.nombre}\nCódigo: {nuevo_curso.get_codigo}\nContraseña: {nuevo_curso.clave}")

        elif opcion == "2":
            print("Cursos dictados:")
            if profesor._Profesor__Cursos:
                for i, curso in enumerate(profesor._Profesor__Cursos, 1):
                    print(f"{i} {curso.nombre}")
                    seleccion = input("Seleccione un curso para ver más detalles (o 'cancelar' para volver al menú): ")
                    if seleccion.lower() == "cancelar":
                        continue
                    elif seleccion.isnumeric() and 1 <= int(seleccion) <= len(profesor._Profesor__Cursos):
                        curso_seleccionado = profesor._Profesor__Cursos[int(seleccion) - 1]
                        print(f"Nombre: {curso_seleccionado.nombre}")
                        print(f"Código: {curso_seleccionado.get_codigo}")
                        print(f"Contraseña: {curso_seleccionado.clave}")
                        print(f"Cantidad de archivos: {len(curso_seleccionado.archivos)}")
                        
                        agregar_archivo = input("¿Desea agregar un archivo adjunto? (Sí/No): ").strip().lower()
                        if agregar_archivo == "si":
                            nombre_archivo = input("Nombre del archivo: ")
                            formato_archivo = input("Formato del archivo: ")
                            archivo = Archivo(nombre_archivo, formato_archivo)
                            curso_seleccionado.archivos.append(archivo)
                            print("Archivo agregado exitosamente.")
                else:
                    print("Opción inválida.")

        elif opcion == "3":
            break

        else:
            print("Opción no válida.")

