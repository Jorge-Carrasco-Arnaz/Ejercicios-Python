# Descripción: Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡Hola <nombre>!
# Entrada: Un nombre
# Salida: Un saludo con el nombre introducido

nombre = input("Introduce tu nombre: ") # Pide al usuario su nombre

def saludo(nombre): # Define la función saludo
    print("¡Hola", nombre, "!") # Imprime el saludo

print(saludo(nombre)) # Imprime el saludo