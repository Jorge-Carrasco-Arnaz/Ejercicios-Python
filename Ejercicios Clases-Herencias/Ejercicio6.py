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

marino = Marino() # Crea un objeto de la clase Marino
pulpo = Pulpo() # Crea un objeto de la clase Pulpo
foca = Foca("Hola, soy una Foca!") # Crea un objeto de la clase Foca

marino.hablar() # Muestra el mensaje
pulpo.hablar() # Muestra el mensaje
foca.hablar() # Muestra el mensaje

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 05/02/2026
# Hora: 14:48
