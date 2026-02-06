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

    def getNombre(self): # Define el método getNombre
        return self.nombre # Devuelve el nombre

    def getApellido(self): # Define el método getApellido
        return self.apellido # Devuelve el apellido

    def setNombre(self, nombre): # Define el Setter de nombre
        if nombre != "": # Comprueba que el nombre no esté vacío
            self.nombre = nombre # Asigna el nombre
        else: # Si el nombre está vacío
            print("Error: El nombre no puede estar vacío") # Imprime error

    def setApellido(self, apellido): # Define el Setter de apellido
        if apellido != "": # Comprueba que el apellido no esté vacío
            self.apellido = apellido # Asigna el apellido
        else: # Si el apellido está vacío
            print("Error: El apellido no puede estar vacío") # Imprime error


class Estudiante(Persona): # Define la clase Estudiante que hereda de Persona
    def __init__(self, nombre, apellido, edad, carrera): # Define el constructor
        super().__init__(nombre, apellido) # Llama al constructor de la clase padre
        self.edad = edad # Define el atributo edad
        self.carrera = carrera # Define el atributo carrera

    def mostrar_carrera(self): # Define el método mostrar_carrera
        return f"La carrera del estudiante es: {self.carrera}" # Devuelve la carrera

    def getEdad(self): # Define el método getEdad
        return self.edad # Devuelve la edad

    def getCarrera(self): # Define el método getCarrera
        return self.carrera # Devuelve la carrera

    def setEdad(self, edad): # Define el Setter de edad
        if edad >= 0: # Valida que la edad no sea negativa
            self.edad = edad # Asigna la edad
        else: # Si es negativa
            print("Error: La edad no puede ser negativa") # Imprime error

    def setCarrera(self, carrera): # Definimos el Setter de carrera
        if carrera != "": # Comprueba que la carrera no esté vacía
            self.carrera = carrera # Asigna la carrera
        else: # Si está vacía
            print("Error: La carrera no puede estar vacía") # Imprime error

print("\nEstudiante 1: \n") # Imprime encabezado
Persona1 = Estudiante("Lucas", "Martínez", 20, "Arquitectura") # Creamos el objeto Persona1
print(f"Nombre: {Persona1.getNombre()}, Apellido: {Persona1.getApellido()}, Edad: {Persona1.getEdad()}, Carrera: {Persona1.getCarrera()}") # Comprueba todos los atributos
Persona1.setNombre("Lucas Gabriel") # Cambiamos el nombre 
Persona1.setApellido("Martínez Ruiz") # Cambiamos el apellido
Persona1.setEdad(21) # Cambiamos la edad
Persona1.setCarrera("Ingeniería") # Cambiamos la carrera
print(f"Nombre actualizado: {Persona1.getNombre()}") # Imprime el nombre para confirmar el cambio
print(f"Apellido actualizado: {Persona1.getApellido()}") # Imprime el apellido para confirmar el cambio
print(f"Edad actualizada: {Persona1.getEdad()}") # Imprime la edad para confirmar el cambio
print(Persona1.mostrar_carrera()) # Imprime la nueva carrera para confirmar el cambio

print("\n") # Salto de linea

print("Persona 2: \n") # Imprime encabezado
Persona2 = Persona("Jorge", "Carrasco") # Creamos el objeto Persona2
print(f"Nombre: {Persona2.getNombre()}, Apellido: {Persona2.getApellido()}") # Comprueba todos los atributos
Persona2.setNombre("Jorgito") # Cambiamos el nombre
Persona2.setApellido("") # Intento de poner apellido vacío
print(f"Nombre actualizado: {Persona2.getNombre()}") # Imprime el nombre para confirmar el cambio
print(f"Apellido tras intento fallido: {Persona2.getApellido()}") # Imprime el apellido para confirmar el cambio

print("\n") # Salto de linea

print("Estudiante 3: \n") # Imprime encabezado
Persona3 = Estudiante("Paco", "Perez", 25, "Medicina") # Creamos el objeto Persona3
print(f"Nombre: {Persona3.getNombre()}, Apellido: {Persona3.getApellido()}, Edad: {Persona3.getEdad()}, Carrera: {Persona3.getCarrera()}") # Comprueba todos los atributos
Persona3.setNombre("") # Intento de poner nombre vacio
Persona3.setApellido("") # Intento de poner apellido vacio
Persona3.setEdad(-10) # Intento de poner edad negativa
Persona3.setCarrera("Enfermería") # Cambiamos la carrera
print(f"Nombre tras intento fallido: {Persona3.getNombre()}") # Imprime el nombre para confirmar el cambio
print(f"Apellido tras intento fallido: {Persona3.getApellido()}") # Imprime el apellido para confirmar el cambio
print(f"Edad tras intento fallido: {Persona3.getEdad()}") # Imprime la edad para confirmar el cambio
print(Persona3.mostrar_carrera()) # Imprime la carrera para confirmar el cambio

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 03/02/2026
# Hora: 10:27