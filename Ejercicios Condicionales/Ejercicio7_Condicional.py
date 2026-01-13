# Descripción: Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
# Entrada: La edad y los ingresos mensuales del usuario
# Salida: Un mensaje indicando si el usuario tiene que tributar o no

edad = int(input("Introduzca su edad: ")) # Pide al usuario que introduzca su edad
ingresos= float(input("Introduzca sus ingresos mensuales: ")) # Pide al usuario que introduzca sus ingresos mensuales

if edad >= 16 and ingresos >= 1000: # Comprueba si la edad es mayor o igual a 16 años y si los ingresos son iguales o mayores a 1000€
    print ("Usted DEBE tributar (El gobierno esta muy FELIZ 😁)") # Imprime un mensaje si las condiciones de edad y ingresos se cumplen
else: # Si alguna de las dos condiciones no se cumple
    print ("Usted no debe tributar (Gobierno triste 💔)") # Imprime un mensaje si alguna de las dos condiciones no se cumple

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 13/01/2026 
# Hora: 10:34