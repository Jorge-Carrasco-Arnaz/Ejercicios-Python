# Descripcion: Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos
# el nombre y la nota del alumno. Definir los métodos siguientes métodos:
# a. Inicializar sus atributos,
# b. Imprimir los atributos
# c. Mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

#Entrada: nombre, nota
#Salida: nombre, nota, aprobado o suspenso

class Estudiante: # Definimos la clase Estudiante
    def __init__(self, nombre, nota): # Definimos el constructor
        self.nombre = nombre # Definimos el atributo nombre
        self.nota = nota # Definimos el atributo nota

    def imprimir(self): # Definimos el metodo imprimir
        print("Nombre: ", self.nombre) # Imprime el nombre
        print("Nota: ", self.nota) # Imprime la nota

    def aprobado(self): # Definimos el metodo aprobado
        if self.nota >= 5: # Si la nota es mayor o igual a 5
            print("El alumno:", self.nombre,"esta aprobado") # Imprime el mensaje de aprobado
        else: # Si la nota es menor a 5
            print("El alumno:", self.nombre,"esta suspendido") # Imprime el mensaje de suspenso

    def getNombre(self): # Definimos el metodo getNombre
        return self.nombre # Devuelve el nombre

    def getNota(self): # Definimos el metodo getNota
        return self.nota # Devuelve la nota

    def setNombre(self, nombre): # Definimos el Setter de nombre
        if nombre != "": # Comprueba que el nombre no esté vacío
            self.nombre = nombre # Asigna el nombre
        else: # Si el nombre está vacío
            print("Error: El nombre no puede estar vacío") # Imprime error de validación

    def setNota(self, nota): # Definimos el Setter de nota
        if nota >= 0 and nota <= 10: # Valida que la nota esté entre 0 y 10
            self.nota = nota # Asigna la nota
        else: # Si la nota no es válida
            print("Error: La nota debe estar entre 0 y 10") # Imprime error de validación


print("\nEstudiante 1: \n") # Imprime encabezado
estudiante1 = Estudiante("Jorge", 5) # Creamos el objeto estudiante1
print(f"La nota inicial de {estudiante1.getNombre()} es {estudiante1.getNota()}") # Imprime nombre y nota usando gets
estudiante1.setNota(8) # Cambiamos la nota de estudiante1
print(f"Ahora Jorge tiene una nota de {estudiante1.getNota()}") # Imprime la nota para confirmar el cambio
estudiante1.setNombre("George") # Cambiamos el nombre de estudiante1
print(f"Ahora el estudiante se llama {estudiante1.getNombre()}") # Imprime el nombre para confirmar el cambio
estudiante1.imprimir() # Imprime los atributos actualizados
estudiante1.aprobado() # Imprime si está aprobado o no

print("\n") # Salto de linea

print("Estudiante 2: \n") # Imprime encabezado
estudiante2 = Estudiante("Paco", 4) # Creamos el objeto estudiante2
print(f"La nota inicial de {estudiante2.getNombre()} es {estudiante2.getNota()}") # Imprime nombre y nota usando gets
estudiante2.setNota(11) # Intentamos cambiar la nota a una inválida
print(f"Nota de Paco tras intento fallido: {estudiante2.getNota()}") # Imprime la nota para confirmar que no cambió
estudiante2.setNombre("") # Intentamos cambiar el nombre a uno vacío
print(f"Nombre de Paco tras intento fallido: {estudiante2.getNombre()}") # Imprime el nombre para confirmar que no cambió
estudiante2.imprimir() # Imprime los atributos
estudiante2.aprobado() # Imprime si está aprobado o no

print("\n") # Salto de linea

print("Estudiante 3: \n") # Imprime encabezado
estudiante3 = Estudiante("Manolo", 10) # Creamos el objeto estudiante3
print(f"La nota inicial de {estudiante3.getNombre()} es {estudiante3.getNota()}") # Imprime nombre 
estudiante3.setNota(2) # Cambiamos la nota a un suspenso
print(f"Ahora Manolo tiene una nota de {estudiante3.getNota()}") # Imprime la nota
estudiante3.setNombre("Manuel") # Cambiamos el nombre
print(f"Ahora el estudiante se llama {estudiante3.getNombre()}") # Imprime el nombre
estudiante3.imprimir() # Imprime los atributos actualizados
estudiante3.aprobado() # Imprime si está aprobado o no

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 03/02/2026
# Hora: 10:24