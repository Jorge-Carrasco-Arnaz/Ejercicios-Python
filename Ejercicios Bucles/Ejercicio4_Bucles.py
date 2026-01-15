#Descripción: Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas
# Entrada: Un número entero positivo
# Salida: La cuenta atrás desde ese número hasta cero separados por comas

n = int(input("Introduzca un número entero positivo: ")) # Pide al usuario un número entero positivo

for i in range(n, -1, -1): # Recorre todos los números desde n hasta 0 (range (inicio, fin, paso))
    if i == 0: # Si el número es 0, no se muestra la coma a la derecha del número
        print(i) # Imprime el número 0
    else: # Si el número no es 0, se muestra la coma a la derecha del número
        print(i, end=", ") # Muestra todos los números desde n hasta 1 separados por comas 
                           #(el end es para que no salte de línea)

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 15/01/2026 
# Hora: 08:36
