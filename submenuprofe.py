from profesor import *
from curso import Curso
def submenuProfesor(profesor, cursos):
    while True:
        print("\nSub Menu Profesor:")
        print("1. Dictar curso")
        print("2. Ver cursos dictados")
        print("3. Volver al menu principal")
        opcion = input("Elija una opcion: ")
        if opcion == "1":
            nombre_curso = input("Ingrese el nombre del curso: ")
            nuevo_curso = Curso(nombre_curso,)
            profesor.dictarCurso(nuevo_curso)
            cursos.append(nuevo_curso)
            print(f"Curso creado exitosamente:\n{str(nuevo_curso)}")
        elif opcion == "2":
            print("Cursos dictados:")
            if profesor._Profesor__Cursos:
                for curso in profesor._Profesor__Cursos:
                    print(f"Nombre: {curso._Curso__nombre}")
                    print(f"Contraseña de matriculacion: {curso._Curso__clave}")
            else:
                print("No dictaste ningun curso")
        elif opcion == "3":
            break
        else:
            print("opcion no valida")
 
 
