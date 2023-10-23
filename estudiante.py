from codGenerator import generar
from abc import ABC, abstractmethod
from usuario import *
from curso import Curso


class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, legajo: int, anioInscripvion: int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anioInscripvion = anioInscripvion
        self.__cursos = []

    def __str__(self) -> str:
        return f"""{super().__str__()} \nLegajo:{self.__legajo} \nAño de inscripcion: {self.__anioInscripvion} \nCursando: {self.__cursos}"""

    def matricularEnCurso(self, curso: Curso):
        while True:
            curso_seleccionado = input("Ingrese el numero del curso en el que desea matricularse (o 'cancelar' para volver al menu): ")
            if curso_seleccionado.lower() == "cancelar":
                print("Volviendo al menú principal.")
                break
            Validacion = True
            while Validacion:
                if curso_seleccionado.isdigit():
                    curso_seleccionado = int(curso_seleccionado)
                    if 1 <= curso_seleccionado <= len(curso):
                        Validacion = False
                    else:
                        print("Opcion invalida.")
                else:
                    print("Opcion invalida.")

            curso = curso[curso_seleccionado - 1]
            if curso in self._Estudiante__cursos:
                print("Ya estas matriculado en este curso.")
            else:
                print(f"{curso._Curso__clave}") #me dicen el hacker
                clave_matriculacion = input(f"Ingrese la contraseña de matriculacion para {curso._Curso__nombre}: ")
                if clave_matriculacion == curso._Curso__clave:
                    self._Estudiante__cursos.append(curso)
                    print(f"Te has matriculado en {curso._Curso__nombre}.")
                    break
                else:
                    print("Contraseña incorrecta. No puedes matricularte en el curso.")


    def validarCredenciales(self, email: str, contrasenia: str):
        return super().validarCredenciales(email, contrasenia)
