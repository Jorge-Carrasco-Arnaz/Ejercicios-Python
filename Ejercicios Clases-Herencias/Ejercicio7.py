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

    def getNombreU(self): # Define el metodo getNombreU
        return self.nombre_universidad # Devuelve el nombre de la universidad

    def setNombreU(self, nombre_universidad): # Define el Setter de nombre_universidad
        if nombre_universidad != "": # Comprueba que el nombre no esté vacío
            self.nombre_universidad = nombre_universidad # Asigna el nombre
        else: # Si el nombre está vacío
            print("Error: El nombre de la universidad no puede estar vacío") # Imprime error

class Carrera(): # Define la clase Carrera
    def __init__(self, especialidad): # Define el constructor de la clase Carrera
        self.especialidad = especialidad # Define el atributo especialidad

    def getEspecialidad(self): # Define el metodo getEspecialidad
        return self.especialidad # Devuelve la especialidad

    def setEspecialidad(self, especialidad): # Define el Setter de especialidad
        if especialidad != "": # Comprueba que la especialidad no esté vacía
            self.especialidad = especialidad # Asigna la especialidad
        else: # Si la especialidad está vacía
            print("Error: La especialidad no puede estar vacía") # Imprime error

class Estudiante(Carrera, Universidad): # Define la clase Estudiante que hereda de Carrera y Universidad
    def __init__(self, nombre, edad, nombre_universidad, especialidad): # Define el constructor de la clase Estudiante
        Universidad.__init__(self, nombre_universidad) # Llama al constructor de la clase Universidad
        Carrera.__init__(self, especialidad) # Llama al constructor de la carrera
        self.nombre = nombre # Define el atributo nombre
        self.edad = edad # Define el atributo edad

    def getNombre(self): # Define el metodo getNombre
        return self.nombre # Devuelve el nombre del estudiante

    def getEdad(self): # Define el metodo getEdad
        return self.edad # Devuelve la edad del estudiante

    def setNombre(self, nombre): # Define el Setter de nombre
        if nombre != "": # Comprueba que el nombre no esté vacío
            self.nombre = nombre # Asigna el nombre
        else: # Si el nombre está vacío
            print("Error: El nombre del estudiante no puede estar vacío") # Imprime error

    def setEdad(self, edad): # Define el Setter de edad
        if edad >= 0: # Valida que la edad no sea negativa
            self.edad = edad # Asigna la edad
        else: # Si la edad es negativa
            print("Error: La edad no puede ser negativa") # Imprime error

    def mostrar(self): # Define el metodo mostrar
        print(f"El Estudiante {self.nombre} tiene {self.edad} años") # Muestra el nombre y edad del estudiante
        print(f"Estudia en la Universidad: {self.nombre_universidad}") # Muestra el nombre de la universidad
        print(f"Y su especialidad es: {self.especialidad}") # Muestra la especialidad del estudiante

print("Persona 1: \n") # Imprime encabezado
persona1 = Estudiante("Juan", 22, "Universidad Pablo de Olavide", "Ingeniería en Software") # Crea el objeto persona1
print(f"Datos iniciales: {persona1.getNombre()}, {persona1.getEdad()} años, {persona1.getNombreU()}, {persona1.getEspecialidad()}") # Imprime todos los atributos
persona1.setNombre("Juan Carlos") # Cambia el nombre
persona1.setEdad(23) # Cambia la edad
persona1.setNombreU("UPO") # Cambia la universidad
persona1.setEspecialidad("Ciberseguridad") # Cambia la especialidad
persona1.mostrar() # Imprime los atributos para confirmar los cambios

print("\n") # Salto de linea

print("Persona 2 (con errores): \n") # Imprime encabezado
persona2 = Estudiante("Pedro", 25, "Universidad de Sevilla", "Ingeniería Civil") # Crea el objeto persona2
persona2.setEdad(-5) # Intento de poner edad negativa
persona2.setNombreU("") # Intento de poner universidad vacía
print(f"Nombre: {persona2.getNombre()}") # Muestra el nombre
print(f"Edad tras intento fallido: {persona2.getEdad()}") # Imprime la edad para confirmar que cambió
print(f"Universidad tras intento fallido: {persona2.getNombreU()}") # Imprime la universidad para confirmar que cambió
persona2.mostrar() # Muestra los atributos del objeto

print("\n") # Salto de linea

print("Persona 3: \n") # Imprime encabezado
persona3 = Estudiante("Maria", 28, "Universidad de Madrid", "Ingeniería en Telecomunicaciones") # Crea el objeto persona3
print(f"Estudiante: {persona3.getNombre()}") # Muestra el nombre actual
persona3.setNombre("Mariana") # Cambia el nombre
persona3.setEspecialidad("Sistemas") # Cambia la especialidad
print(f"Nombre actualizado: {persona3.getNombre()}") # Imprime para confirmar el cambio
print(f"Especialidad actualizada: {persona3.getEspecialidad()}") # Imprime para confirmar el cambio
persona3.mostrar() # Muestra los atributos finales

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 05/02/2026
# Hora: 14:52