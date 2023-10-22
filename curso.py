from codGenerator import generar
from abc import ABC, abstractmethod

class Curso ():
    def __init__(self,nombreCurso:str):
        self.__nombre= nombreCurso
        self.__clave = self.__generarContraseña()
        
    def __str__(self) -> str:
        return f"""Nombre: {self.__nombre} \n Clave de matriculacion: {self.__clave}"""
    
    @classmethod
    def __generarContraseña(cls):
        return generar()
    
        