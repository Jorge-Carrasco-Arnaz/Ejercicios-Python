# Descripción: Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad). 
# Entrada: Edad dada por el usuario
# Salida: Años cumplidos desde el 1 hasta su edad

edad = int(input("Introduzca su edad: ")) # Pide al usuario su edad
i = 0 # Inicializamos la variable i

for i in range(1, edad + 1): # Creamos el bucle for para que recorra por las edades desde el 1 y sumamos +1 a la edad para que añada la edad actual
    print("Has cumplido: ",i, "años 🎉") # Imprimimos por pantalla el mensaje que habrá en bucle sobre los años cumplidos por el usuario

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 13/01/2026 
# Hora: 11:08
