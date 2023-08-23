class Persona:
    def __init__(self, nombre="", edad=0, dni=0):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        if type(value) is str:
            self.__nombre = value
        else:
            print("Error: el nombre debe tener sólo caracteres alfabéticos")
            self.__nombre = ""

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, value):
        if type(value) is int and 0 <= value <= 150:
            self.__edad = value
        else:
            print("Error: la edad debe ser un número entero entre 0 y 150")
            self.__edad = ""

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, value):
        if type(value) is int and 1000000 <= value <= 99999999:
            self.__dni = value
        else:
            print("Error: el DNI debe ser un número entero entre 1000000 y 99999999")
            self._dni = ""

    def mostrar(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.dni}")

    def es_mayor_de_edad(self):
        return self.edad >= 18
