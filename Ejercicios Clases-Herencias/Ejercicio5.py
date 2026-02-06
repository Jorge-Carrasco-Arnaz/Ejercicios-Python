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

    def getLlantas(self): # Define el metodo getLlantas
        return self.llantas # Devuelve la cantidad de llantas

    def getColor(self): # Define el metodo getColor
        return self.color # Devuelve el color

    def getPrecio(self): # Define el metodo getPrecio
        return self.precio # Devuelve el precio

    def setLlantas(self, llantas): # Define el Setter de llantas
        if llantas > 0: # Valida que la cantidad sea mayor a 0
            self.llantas = llantas # Asigna la cantidad de llantas
        else: # Si es 0 o menor
            print("Error: La cantidad de llantas debe ser mayor a 0") # Imprime error

    def setColor(self, color): # Define el Setter de color
        if color != "": # Comprueba que el color no este vacio
            self.color = color # Asigna el color
        else: # Si el color esta vacio
            print("Error: El color no puede estar vacio") # Imprime error

    def setPrecio(self, precio): # Define el Setter de precio
        if precio >= 0: # Valida que el precio no sea negativo
            self.precio = precio # Asigna el precio
        else: # Si el precio es negativo
            print("Error: El precio no puede ser negativo") # Imprime error

class Moto(Fabrica): # Define la clase Moto que hereda de Fabrica
    def __init__(self, llantas, color, precio): # Define el constructor de la clase Moto
        super().__init__(llantas, color, precio) # Llama al constructor de la clase padre

class Carro(Fabrica): # Define la clase Carro que hereda de Fabrica
    def __init__(self, llantas, color, precio): # Define el constructor de la clase Carro
        super().__init__(llantas, color, precio) # Llama al constructor de la clase padre


print("\nObjeto 1 (Moto y Carro): \n") # Imprime encabezado
moto1 = Moto(2, "Negro", 1500) # Crea un objeto de la clase Moto
carro1 = Carro(4, "Rojo", 2500) # Crea un objeto de la clase Carro
print(f"Moto 1 - Llantas: {moto1.getLlantas()}, Color: {moto1.getColor()}, Precio: {moto1.getPrecio()}") # Imprime atributos de moto1
print(f"Carro 1 - Llantas: {carro1.getLlantas()}, Color: {carro1.getColor()}, Precio: {carro1.getPrecio()}") # Imprime atributos de carro1
moto1.setPrecio(1600) # Cambiamos el precio de la moto
carro1.setColor("Verde") # Cambiamos el color del carro
print(f"Moto 1 Precio Actualizado: {moto1.getPrecio()}") # Imprime el precio para confirmar el cambio
print(f"Carro 1 Color Actualizado: {carro1.getColor()}") # Imprime el color para confirmar el cambio

print("\n") # Salto de linea

print("Objeto 2 (Moto y Carro con errores): \n") # Imprime encabezado
moto2 = Moto(1, "Marrón", 100) # Crea un objeto de la clase Moto
carro2 = Carro(4, "Kiwi", 200) # Crea un objeto de la clase Carro
moto2.setLlantas(0) # Intento de poner 0 llantas
carro2.setPrecio(-500) # Intento de poner precio negativo
print(f"Moto 2 Llantas tras intento fallido: {moto2.getLlantas()}") # Imprime las llantas para confirmar que no cambió
print(f"Carro 2 Precio tras intento fallido: {carro2.getPrecio()}") # Imprime el precio para confirmar que no cambió
moto2.mostrar() # Muestra atributos de moto2
carro2.mostrar() # Muestra atributos de carro2

print("\n") # Salto de linea

print("Objeto 3 (Moto y Carro): \n") # Imprime encabezado
moto3 = Moto(3, "Azul", 200) # Crea un objeto de la clase Moto
carro3 = Carro(4, "Azul", 40000) # Crea un objeto de la clase Carro
moto3.setLlantas(2) # Cambiamos llantas
moto3.setColor("Blanco") # Cambiamos color
moto3.setPrecio(500) # Cambiamos precio
carro3.setLlantas(4) # Cambiamos llantas
carro3.setColor("Plata") # Cambiamos color
carro3.setPrecio(45000) # Cambiamos precio
print(f"Moto 3 - Llantas: {moto3.getLlantas()}, Color: {moto3.getColor()}, Precio: {moto3.getPrecio()}") # Imprime los atributos para confirmar el cambio
print(f"Carro 3 - Llantas: {carro3.getLlantas()}, Color: {carro3.getColor()}, Precio: {carro3.getPrecio()}") # Imprime los atributos para confirmar el cambio

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 05/02/2026
# Hora: 14:41