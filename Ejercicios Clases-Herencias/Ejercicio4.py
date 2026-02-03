# Descripcion: Crear una clase “Persona” que sea la clase padre de otra clase “Estudiante”. Por tanto: En la
# clase “Persona” su método __init__() debe de estar preparado para recibir nombre y apellido.
# Además, esta clase, debe tener un método para mostrar nombre_completo() el cual debe
# mostrar el nombre acompañado del apellido.
# La otra clase “Estudiante”, debe de poder heredar de “Persona”, y además recibir los argumentos
# nombre y edad. También la clase “Estudiante”, recibe el valor “carrera”, y además contar con un
# método mostrar_carrera(). Las dos clases son obligatorias.

#Entrada: nombre, apellido, nombre, edad, carrera
#Salida: nombre_completo(), mostrar_carrera()

class Persona: # Define la clase Persona
    def __init__(self, nombre, apellido): # Define el constructor
        self.nombre = nombre # Define el atributo nombre
        self.apellido = apellido # Define el atributo apellido
    
    def nombre_completo(self): # Define el metodo nombre_completo
        return f"Nombre completo: {self.nombre} {self.apellido}" # Devuelve el nombre y el apellido


class Estudiante(Persona): # Define la clase Estudiante que hereda de Persona
    def __init__(self, nombre, apellido, edad, carrera): # Define el constructor
        super().__init__(nombre, apellido) # Llama al constructor de la clase padre
        self.edad = edad # Define el atributo edad
        self.carrera = carrera # Define el atributo carrera

    def mostrar_carrera(self): # Define el metodo mostrar_carrera
        return f"La carrera del estudiante es: {self.carrera}" # Devuelve la carrera


Persona1 = Estudiante("Lucas", "Martínez", 20, "Arquitectura") # Creamos el objeto Persona1

print(Persona1.nombre_completo()) # Imprime el nombre completo
print(Persona1.mostrar_carrera()) # Imprime la carrera
print("\n") # Salto de linea

Persona2 = Persona("Jorge", "Carrasco") # Creamos el objeto Persona2

print(Persona2.nombre_completo()) # Imprime el nombre completo
print("\n") # Salto de linea

# print(Persona2.mostrar_carrera()) No se puede utilizar en este objeto porque el constructor que usamos no es el de Estudiante, 
# por lo tanto no tiene el atributo carrera

Persona3 = Estudiante("Paco", "Perez", 25, "Medicina") # Creamos el objeto Persona3

print(Persona3.nombre_completo()) # Imprime el nombre completo
print(Persona3.mostrar_carrera()) # Imprime la carrera
print("\n") # Salto de linea

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 03/02/2026
# Hora: 10:27