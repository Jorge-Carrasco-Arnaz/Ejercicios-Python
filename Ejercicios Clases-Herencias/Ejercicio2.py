# Descripción: Crea una clase “Persona”. Con atributos nombre y edad. .
# Definir los siguientes métodos:
# a. Inicializar sus atributos
# b. Método “cumpleaños”, que aumente en 1 la edad de la persona cuando se invoque sobre un objeto creado con “Persona”
# c. Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# d. mostrar(): Muestra los datos de la persona.
# e. esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

# Entrada:
# Salida: 

class Persona: # Definimos la clase Persona
    def __init__(self, nombre, edad): # Definimos el constructor
        self.nombre = nombre # Definimos el atributo nombre
        self.edad = edad # Definimos el atributo edad

    def cumpleaños(self): # Definimos el metodo cumpleaños
        self.edad += 1 # Aumenta la edad en 1

    def getNombre(self): # Definimos el metodo getNombre
        return self.nombre # Devuelve el nombre

    def getEdad(self): # Definimos el metodo getEdad
        return self.edad # Devuelve la edad

    def setNombre(self, nombre): # Definimos el Setter de nombre
        self.nombre = nombre # Asigna el nombre

    def setEdad(self, edad): # Definimos el Setter de edad
        self.edad = edad # Asigna la edad

    def esMayorDeEdad(self): # Definimos el metodo esMayorDeEdad

        if self.edad < 0: # Si la edad es menor a 0
            return "La edad no puede ser negativa"
        elif self.edad < 18: # Si la edad es menor a 18
            return "No es mayor de edad"
        else: # Si la edad es mayor o igual a 18
            return "Es mayor de edad"

p1=Persona("Jorge", 20) # Creamos el objeto p1
print(f"Antes de su cumpleaños {p1.getNombre()} tiene {p1.getEdad()} años") # Imprime el nombre y la edad
p1.setEdad(40) # Cambiamos la edad de p1
print(f"Ahora Jorge tiene {p1.getEdad()}") # Imprime la edad de p1 para confirmar el cambio
p1.setNombre("Kyle") # Cambiamos el nombre p1
print(f"Ahora Jorge tiene el nombre {p1.getNombre()}") # Imprime el nombre p1 para confirmar el cambio
p1.cumpleaños() # Aumenta la edad en 1
print(f"Después de su cumpleaños {p1.getNombre()} tiene {p1.getEdad()} años") # Imprime el nombre y la edad
print(p1.esMayorDeEdad()) # Imprime si es mayor de edad

print("\n") # Salto de linea

p2=Persona("Paco", 15) # Creamos el objeto p2
print(f"Antes de su cumpleaños {p2.getNombre()} tiene {p2.getEdad()} años") # Imprime el nombre y la edad
p2.setEdad(16) # Cambiamos la edad de p2
print(f"Ahora Paco tiene {p2.getEdad()}") # Imprime la edad de p2 para confirmar el cambio
p2.setNombre("Lola") # Cambiamos el nombre p2
print(f"Ahora Paco tiene el nombre {p2.getNombre()}") # Imprime el nombre p2 para confirmar el cambio
p2.cumpleaños() # Aumenta la edad en 1
print(f"Después de su cumpleaños {p2.getNombre()} tiene {p2.getEdad()} años") # Imprime el nombre y la edad
print(p2.esMayorDeEdad()) # Imprime si es mayor de edad

print("\n") # Salto de linea

p3=Persona("Manolo", -2) # Creamos el objeto p3
print(f"Antes de su cumpleaños {p3.getNombre()} tiene {p3.getEdad()} años") # Imprime el nombre y la edad
p3.setEdad(-10) # Cambiamos la edad de p3
print(f"Ahora Manolo tiene {p3.getEdad()}") # Imprime la edad de p3 para confirmar el cambio
p3.setNombre("Karlita") # Cambiamos el nombre p3
print(f"Ahora Manolo tiene el nombre {p3.getNombre()}") # Imprime el nombre p3 para confirmar el cambio
p3.cumpleaños() # Aumenta la edad en 1
print(f"Después de su cumpleaños {p3.getNombre()} tiene {p3.getEdad()} años") # Imprime el nombre y la edad
print(p3.esMayorDeEdad()) # Imprime si es mayor de edad

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 03/02/2026
# Hora: 10:23

