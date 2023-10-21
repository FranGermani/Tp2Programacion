from codGenerator import generar
from abc import ABC, abstractmethod

class Usuario (ABC):
    def __init__(self,nombre: str, apellido: str, email: str, contrasenia: str):
        self.__nombre = nombre
        self.__apellido= apellido
        self.__email= email
        self.__contrasenia= contrasenia
        
    def __str__(self) -> str:
        return f"""\n Nombre:{self.__nombre}\n Apellido:{self.__apellido}\n Email:{self.__email}\n contraseña:{self.__contrasenia}"""
    
    @abstractmethod
    def validarCredenciales(self,email: str,contrasenia: str):
        pass
        