# Descripción: Desarrollar un programa con tres clases: La primera debe ser Universidad, 
# con atributos nombre (Donde se almacena el nombre de la Universidad). La segunda llamada Carerra, 
# con los atributos especialidad (En donde me guarda la especialidad de un estudiante). 
# Y por último, una llamada Estudiante, que tenga como atributos su nombre y edad. 
# El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.

# Entrada: nombre, especialidad, edad
# Salida: nombre, especialidad, edad, universidad


class Universidad(): # Define la clase Universidad
    def __init__(self, nombre_universidad): # Define el constructor de la clase Universidad
        self.nombre_universidad = nombre_universidad # Define el atributo nombre_universidad

class Carrera(): # Define la clase Carrera
    def __init__(self, especialidad): # Define el constructor de la clase Carrera
        self.especialidad = especialidad # Define el atributo especialidad

class Estudiante(Carrera, Universidad): # Define la clase Estudiante que hereda de Carrera y Universidad
    def __init__(self, nombre, edad, nombre_universidad, especialidad): # Define el constructor de la clase Estudiante
        Universidad.__init__(self, nombre_universidad) # Llama al constructor de la clase Universidad
        Carrera.__init__(self, especialidad) # Llama al constructor de la clase Carrera
        self.nombre = nombre # Define el atributo nombre
        self.edad = edad # Define el atributo edad

    def mostrar(self): # Define el metodo mostrar
        print(f"El Estudiante {self.nombre} tiene {self.edad} años") # Muestra el nombre y edad del estudiante
        print(f"Estudia en la Universidad: {self.nombre_universidad}") # Muestra el nombre de la universidad
        print(f"Y su especialidad es: {self.especialidad}") # Muestra la especialidad del estudiante

persona1 = Estudiante("Juan", 22, "Universidad Pablo de Olavide", "Ingeniería en Software") # Crea un objeto de la clase Estudiante
persona1.mostrar() # Muestra los atributos del objeto

print("\n") # Salto de linea

persona2 = Estudiante("Pedro", 25, "Universidad de Sevilla", "Ingeniería Civil") # Crea un objeto de la clase Estudiante
persona2.mostrar() # Muestra los atributos del objeto

print("\n") # Salto de linea

persona3 = Estudiante("Maria", 28, "Universidad de Madrid", "Ingeniería en Telecomunicaciones") # Crea un objeto de la clase Estudiante
persona3.mostrar() # Muestra los atributos del objeto

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 05/02/2026
# Hora: 14:52
