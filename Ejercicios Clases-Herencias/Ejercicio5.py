# Descripcion: Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases más que hereden de Fabrica,
# las cuales son Moto y Carro.
# Crear métodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
# Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno.

# Entrada: Llantas, Color, Precio
# Salida: cantidad de llantas, color y precio de ambos transportes

class Fabrica: # Define la clase Fabrica
    def __init__(self, llantas, color, precio): # Define el constructor de la clase Fabrica
        self.llantas = llantas # Define el atributo llantas
        self.color = color # Define el atributo color
        self.precio = precio # Define el atributo precio

    def mostrar(self): # Define el metodo mostrar de la clase Fabrica
        print(f"Cantidad de llantas: {self.llantas}") # Muestra la cantidad de llantas
        print(f"Color: {self.color}") # Muestra el color
        print(f"Precio: {self.precio}") # Muestra el precio

class Moto(Fabrica): # Define la clase Moto que hereda de Fabrica
    def __init__(self, llantas, color, precio): # Define el constructor de la clase Moto
        super().__init__(llantas, color, precio) # Llama al constructor de la clase padre

class Carro(Fabrica): # Define la clase Carro que hereda de Fabrica
    def __init__(self, llantas, color, precio): # Define el constructor de la clase Carro
        super().__init__(llantas, color, precio) # Llama al constructor de la clase padre

moto1 = Moto(2, "Negro", 1500) # Crea un objeto de la clase Moto
carro1 = Carro(4, "Rojo", 2500) # Crea un objeto de la clase Carro

moto1.mostrar() # Muestra los atributos de la clase Moto
carro1.mostrar() # Muestra los atributos de la clase Carro

print("\n") # Salto de linea

moto2 = Moto(1, "Marrón", 100) # Crea un objeto de la clase Moto
carro2 = Carro(4, "Kiwi", 200) # Crea un objeto de la clase Carro

moto2.mostrar() # Muestra los atributos de la clase Moto
carro2.mostrar() # Muestra los atributos de la clase Carro

print("\n") # Salto de linea

moto3 = Moto(3, "Azul", 200) # Crea un objeto de la clase Moto
carro3 = Carro(4, "Azul", 40000) # Crea un objeto de la clase Carro

print("\n") # Salto de linea

moto3.mostrar() # Muestra los atributos de la clase Moto
carro3.mostrar() # Muestra los atributos de la clase Carro

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 05/02/2026
# Hora: 14:41
