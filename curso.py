from codGenerator import generar
from abc import ABC, abstractmethod
from archivo import Archivo
from carrera import Carrera

class Curso():
    prox_num = 0

    def __init__(self, nombreCurso: str, carrera: Carrera):
        self.__nombre = nombreCurso
        self.__clave = self.__generarContrasenia()
        self.__codigo = self.codigo()
        self.__archivos = []
        self.__carrera = carrera

    def __str__(self) -> str:
        return f"Nombre: {self.__nombre} \nClave de matriculación: {self.__clave}"

    @classmethod
    def __generarContrasenia(cls):
        return generar()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def clave(self):
        return self.__clave

    @classmethod
    def codigo(cls):
        cls.prox_num += 1
        return cls.prox_num

    @property
    def get_codigo(self):
        return self.__codigo

    @property
    def carrera(self):
        return self.__carrera

    @property
    def archivos(self):
        return self.__archivos
