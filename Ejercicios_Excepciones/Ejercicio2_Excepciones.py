# Descripción: Crear una función mas_10(num) que devuelva el número añadiéndole 10. Crear un programa que pida un número, 
# llame a la función mas_10 y muestre su resultado. Controlar el error si le introducimos una variable de otro tipo.
# Entrada: Un número
# Salida: El número + 10 o un mensaje de error si se introduce otro tipo de variable


def mas_10(num): # Función que suma 10 al número
    try: # Intenta sumar 10 al número
        return f"El resultado de sumarle 10 al número es: {float(num) + 10}" # Devuelve el número + 10
    except ValueError: # Si se produce un error al sumar 10, devuelve un mensaje de error
        return "Error: Picha que no puedes sumar 10 a una variable de otro tipo 😵‍💫" # Mensaje de error

num = input("Introduce un número: ") # Pide al usuario un número

print(mas_10(num)) # Imprime el resultado de sumarle 10 al número o el mensaje de error

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 27/01/2026
# Hora: 10:42