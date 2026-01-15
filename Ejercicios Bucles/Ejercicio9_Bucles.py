# Descripción: Escribir un programa que pida al usuario una palabra 
# y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
# Entrada: Una palabra dada por el usuario
# Salida: Las letras de la palabra introducida empezando por la última

palabra = str(input("Introduzca una palabra: ")) # Pide al usuario una palabra

for i in reversed(palabra): # Recorre la palabra carácter por carácter de forma inversa
                             # (El encargado es la función reversed que lo que hace es dar la vuelta a la cadena)
    print(i) # Muestra los caracteres de la palabra de forma inversa

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 15/01/2026 
# Hora: 10:03
