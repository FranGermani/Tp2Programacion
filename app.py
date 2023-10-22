import os
from submenuAlumn import subMenuAlumno
from submenuprofe import submenuProfesor
from profesor import Profesor
from estudiante import Estudiante
from usuario import Usuario

alumnos = []
profesores = []
cursos = []

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
                subMenuAlumno(estudiante)
            else:
                print("Error de ingreso")
        elif int(opt) == 2:
            email = input("Correo: ")
            contrasenia = input("contrasenia: ")
            profesor = None
            for profe in profesores:
                if profe.validarCredenciales(email, contrasenia):
                    profesor = profe
                    break

            if profesor is not None:
                submenuProfesor(profesor)
            else:
                print("Error de ingreso")
        elif int(opt) == 3:
            print("asd")
        elif int(opt) == 4:
            opcion = "salir"
        else:
            print("Ingrese una opcion valida")
    else:
        print("Ingrese una opcion numerica")

    input("Presione Enter para continuar...")  # Pausa

print("¡Hasta luego!")
