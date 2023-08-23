from actEjer6_Persona import Persona
from actEjer7_Cuenta import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, titular: Cuenta, bonificacion=0):
        self.__titular =  f"{Cuenta.titular} {Cuenta.cantidad}"
        self.__bonificacion = bonificacion
        
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, value):
        if isinstance(value, Cuenta):
            self.__titular = value
        else:
            print("Error: el titular debe estar registrada")
            self.__titular = ""
            
    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, value):
        if type(value) is int or type(value) is float:
            self.__bonificacion = value
        else:
            print("Error: la bonificación debe ser un porcentaje")

    def es_titular_valido(self):
        return self.persona.es_mayor_de_edad() and self.persona.edad < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            Cuenta.retirar(self, cantidad)

    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print(f"Bonificación: {self.bonificacion}%")
