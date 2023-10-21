from codGenerator import generar
from abc import ABC, abstractmethod
from usuario import *
from curso import Curso

class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, legajo:int, anioInscripvion:int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anioInscripvion = anioInscripvion
        self.__cursos=[]
    
    def __str__(self) -> str:
        return f"""{super().__str__()} \nLegajo:{self.__legajo} \nAño de inscripcion: {self.__anioInscripvion} \nCursando: {self.__cursos}"""
    
    def matricularEnCurso (curso:Curso):
        pass