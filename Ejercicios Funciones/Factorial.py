# Descripción: Escribir una función que recibe un número entero positivo y devuelva su factorial.
# Entrada: Un número positivo
# Salida: El factorial del número

def factorial(numero): # Define la función factorial
    
    if (numero >= 0): # Comprueba si el número es positivo
        resultado = 1 # Inicializa la variable resultado a 1
        for i in range (1,numero+1): # Bucle que recorre desde el número introducido hasta 1
            resultado *= i # *= es lo mismo que resultado = resultado * i
        return resultado # Devuelve el resultado
    else: # Si el número no es positivo
        print ("El número introudcido no es positivo") # Imprime un mensaje de error

numero = int(input("Introduce un numero positivo: ")) # Pide al usuario un número positivo

print("La media es de: "factorial(numero)) # Imprime el resultado
