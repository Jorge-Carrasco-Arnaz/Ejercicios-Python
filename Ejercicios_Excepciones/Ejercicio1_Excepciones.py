# Descripción: Crear un programa que pida dos números a un usuario y devuelva su división. 
# Deberás programar también la función para dividir que recibiendo esos dos números devuelva el resultado de su división. 
# Tendrás que controlar también el error que obtienes al dividir entre cero. 
# Entrada: Dos números
# Salida: División de los dos números o un mensaje de error si se divide entre cero

n1 = int(input("Introduce el primer número: ")) # Pide al usuario el primer número
n2 = int(input("Introduce el segundo número: ")) # Pide al usuario el segundo número

def dividir(n1, n2): # Función que divide dos números
    try: # Intenta dividir los dos números
        return n1 / n2 # Devuelve el resultado de la división
    except ZeroDivisionError: # Si se produce un error al dividir entre cero, devuelve un mensaje de error
        return "Error: Picha que no puedes dividir entre 0, vas a abrir un agujero negro 😵‍💫" # Mensaje de error

print("El resultado de la división es: ", dividir(n1, n2)) # Imprime el resultado de la división

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 27/01/2026
# Hora: 10:07
