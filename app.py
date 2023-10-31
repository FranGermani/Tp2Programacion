import os
from submenuAlumn import subMenuAlumno
from submenuprofe import submenuProfesor
from profesor import Profesor
from estudiante import Estudiante
from usuario import Usuario
from curso import *

codigo_admin= "admin123"
contrasenia_admin="admin123"
alumnos = []
profesores = []
cursos = []


nombres_de_cursos = ["Programación I", "Programación II", "Programación III", "Ingles I", "Ingles II", "Matemática", "Laboratorio I", "Laboratorio II", "Laboratorio III", "Laboratorio IV", "Sistema de Procesamiento de Datos", "Arquitectura y Sistemas Operativos", "Metodologia de la Investigacion", "Organizacion Contable de la Empresa", "Organizacion Empresarial", "Elementos de Investigación Operativa", "Legislacion", "Diseño y Administracion de Bases de Datos", "Metodologias de Sistemas"]

for nombre_curso in nombres_de_cursos:
    nuevo_curso = Curso(nombre_curso, "Tecnicatura Universitaria en Programación")
    cursos.append(nuevo_curso)


alumnos.append(Estudiante("francisco", "germani","franciscogermani@hotmail.com", "123", 213213, 1998))
profesores.append(Profesor("Mechi", "Nomeacuerdoperdon","tampoco@hotmail.com", "213", "programadora", 1998))
profesores.append(Profesor("Miguel", "Menos","qcsho@hotmail.com", "213", "programador", 1990))
#asi con todos los profes
print("Bienvenido!")
opcion = ''


def menu():
    print("Menu Principal:")
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")


while opcion != "salir":
    menu()
    opt = input("\nIngrese la opcion del menu: ")
    os.system("cls")

    if opt.isnumeric():
        if int(opt) == 1:
            email = input("Correo: ")
            contrasenia = input("contrasenia: ")
            estudiante = None
            for alumno in alumnos:
                if alumno.validarCredenciales(email, contrasenia):
                    estudiante = alumno
                    break

            if estudiante is not None:
                subMenuAlumno(estudiante, cursos)
            else:
                print("Error de ingreso,verifica tus credenciales o dale de alta en alumnado.")
        elif int(opt) == 2:
            email = input("Correo: ")
            contrasenia = input("contrasenia: ")
            
            if email == codigo_admin:
                contrasenia_admin = input("Contraseña de administrador: ")
                if contrasenia_admin == contrasenia_admin:
                    nuevo_profesor = Profesor(input("Nuevo profesor - Nombre: "), input("Nuevo profesor - Apellido: "), input("Nuevo profesor - Correo: "), input("Nuevo profesor - Contraseña: "), input("Nuevo profesor - Título: "), input("Nuevo profesor - Año de Egreso: "))
                    profesores.append(nuevo_profesor)
                    print("Nuevo profesor dado de alta exitosamente.")
                    continue
            profesor = None
            for profe in profesores:
                if profe.validarCredenciales(email, contrasenia):
                    profesor = profe
                    break
            if profesor is not None:
                submenuProfesor(profesor, cursos)
            else:
                print("Error de ingreso")


        elif int(opt) == 3:
              print("Lista de Cursos:")
              sorted_cursos = sorted(cursos, key=lambda curso: curso._Curso__nombre)
              for curso in sorted_cursos:
                  print(f"Materia: {curso._Curso__nombre} Carrera: Tecnicatura Universitaria en Programacion")
        elif int(opt) == 4:
            opcion = "salir"
        else:
            print("Ingrese una opcion valida")
    else:
        print("Ingrese una opcion numerica")

    input("Presione Enter para continuar...")  # Pausa

print("¡Hasta luego!")
