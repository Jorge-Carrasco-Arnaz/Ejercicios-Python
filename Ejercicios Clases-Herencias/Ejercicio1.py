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

estudiante1 = Estudiante("Jorge", 5) # Creamos el objeto estudiante1
estudiante1.imprimir() # Imprime el nombre y la nota
estudiante1.aprobado() # Imprime si el alumno esta aprobado o suspenso

estudiante2 = Estudiante("Paco", 4) # Creamos el objeto estudiante2
estudiante2.imprimir() # Imprime el nombre y la nota
estudiante2.aprobado() # Imprime si el alumno esta aprobado o suspenso

estudiante3 = Estudiante("Manolo",10) # Creamos el objeto estudiante3
estudiante3.imprimir() # Imprime el nombre y la nota
estudiante3.aprobado() # Imprime si el alumno esta aprobado o suspenso

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 03/02/2026
# Hora: 10:24
