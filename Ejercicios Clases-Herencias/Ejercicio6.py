# Descripcion: Crear una clase llamada Marino(), con un método que sea hablar, en donde muestre un mensaje que diga «Hola, soy un animal marino!». 
# Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por «Hola soy un Pulpo!».
# Por último, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo llamado mensaje y que muestre ese mensaje como parámetro.

# Entrada: Mensaje
# Salida: Mensaje

class Marino(): # Define la clase Marino
    def hablar(self): # Define el método hablar
        print("Hola, soy un animal marino!") # Muestra el mensaje

class Pulpo(Marino): # Define la clase Pulpo que hereda de Marino
    def hablar(self): # Define el método hablar
        print("Hola, soy un Pulpo!") # Muestra el mensaje

class Foca(Marino): # Define la clase Foca que hereda de Marino
    def __init__(self, mensaje): # Define el constructor de la clase Foca
        self.mensaje = mensaje # Define el atributo mensaje

    def hablar(self): # Define el método hablar
        print(self.mensaje) # Muestra el mensaje

    def getMensaje(self): # Define el método getMensaje
        return self.mensaje # Devuelve el mensaje

    def setMensaje(self, mensaje): # Define el Setter de mensaje
        if mensaje != "": # Comprueba que el mensaje no esté vacío
            self.mensaje = mensaje # Asigna el mensaje
        else: # Si el mensaje está vacío
            print("Error: El mensaje no puede estar vacío") # Imprime error

print("\nObjeto 1 (Marino): \n") # Imprime encabezado
animal1 = Marino() # Crea un objeto de la clase Marino
animal1.hablar() # Muestra el mensaje original

print("\nObjeto 2 (Pulpo): \n") # Imprime encabezado
animal2 = Pulpo() # Crea un objeto de la clase Pulpo
animal2.hablar() # Muestra el mensaje modificado por herencia

print("\nObjeto 3 (Foca): \n") # Imprime encabezado
animal3 = Foca("Hola, soy una Foca!") # Crea un objeto de la clase Foca
print(f"Mensaje inicial: {animal3.getMensaje()}") # Imprime el mensaje usando get
animal3.hablar() # Muestra el mensaje a través del método hablar
animal3.setMensaje("Nuevo mensaje para la foca") # Cambiamos el mensaje con el setter
print(f"Mensaje actualizado: {animal3.getMensaje()}") # Imprime el mensaje para confirmar el cambio
animal3.hablar() # Muestra el mensaje actualizado

print("\nPrueba de error en Foca: \n") # Imprime encabezado
animal3.setMensaje("") # Intento de poner un mensaje vacío
print(f"Mensaje tras intento fallido: {animal3.getMensaje()}") # Imprime el mensaje para confirmar que no cambió

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 05/02/2026
# Hora: 14:48