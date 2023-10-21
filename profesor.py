from codGenerator import generar
from abc import ABC, abstractmethod
from usuario import *
from curso import *

class Profesor(Usuario):
    
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str, anioEgreso:int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo= titulo
        self.__anioEgreso= anioEgreso
        self.__Cursos= []
        
    def __str__(self) -> str:
        return f"""{super().__str__()} \n Titulo:{self.__titulo} \n Año egreso:{self.__anioEgreso} \n curso: {self.__Cursos}"""
    
    def dictarCurso (self, curso:Curso):
        pass