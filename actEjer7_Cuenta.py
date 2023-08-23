from actEjer6_Persona import Persona

class Cuenta(Persona):
    def __init__(self, titular: Persona, cantidad=0):
        self.__titular =  f"{Persona.nombre} {Persona.edad} {Persona.dni}"
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, value):
        if isinstance(value, Persona):
            self.__titular = value
        else:
            print("Error: el titular debe estar registrada")
            self.__titular = ""

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, value):
        if type(value) is int or type(value) is float:
            self.__cantidad = value
        else:
            print("Error: la cantidad debe ser un número")

    def mostrar(self):
        print(f"Titular: {self.titular}\nCantidad: {self.cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
