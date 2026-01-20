# Descripción: Escribir una función que calcule el área de un círculo y otra que calcule el volumen
# de un cilindro usando la primera función
# Entrada: Radio y altura
# Salida: Área y volumen

import math # Importa la librería math para poder usar el número pi

def area (rad): # Define la función area
    area = math.pi * rad**2 # Calcula el area donde math.pi es el número pi y los ** es el elevado
    return round (area,2) # Devuelve el area 

def volumen (alt, rad): # Define la función volumen
    volumen = area(rad) * alt # Calcula el area usando el resultado de la función area 

    return round(volumen,2) # Devuelve el volumen con dos decimales


radio = float(input("Introduce el radio: ")) # Pide al usuario el radio
altura = float(input("Introduce la altura: ")) # Pide al usuario la altura

print("El área del círculo es de: ", area(radio)) # Imprime el area del círculo
print("El volumen del cilindro es de: ", volumen(altura,radio)) # Imprime el volumen del cilindro