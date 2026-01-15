#Descripción: Escribir un programa que pida al usuario un número entero positivo 
#y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas
#Entrada: Un número entero positivo
#Salida: Todos los números impares desde 1 hasta ese número separados por comas

n = int(input("Introduzca un número entero positivo: ")) # Pide al usuario un número entero positivo
for i in range(1, n+1, 2): # Recorre todos los números impares desde 1 hasta n (range (inicio, fin, paso))
    print(i, end=", ") # Muestra todos los números impares desde 1 hasta n separados por comas 
                       # (el end es para que no salte de línea)

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 15/01/2026 
# Hora: 08:26

