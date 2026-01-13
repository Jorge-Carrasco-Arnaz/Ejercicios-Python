# Descripción: Solicitar al usuario que ingrese tres numeros y mostrar cual es el mayor de los tres. 
# Entrada: Tres números dados por el usuario
# Salida: Mensaje indicando cuál de los tres números es el mayor

n1 = int(input("Introduzca el primer número: ")) # Pide al usuario el primer número
n2 = int(input("Introduzca el segundo número: ")) # Pide al usuario el segundo número
n3 = int(input("Introduzca el tercer número: ")) # Pide al usuario el tercer número

if n1 > n2 and n1 > n3: # Comprueba si el primer número es mayor que el segundo y el tercero
    print("El primer número es el mayor de los tres") # Muestra el mensaje de que el primer número es el mayor
elif n2 > n1 and n2 > n3: # Comprueba si el segundo número es mayor que el primer y el tercero
    print("El segundo número es el mayor de los tres") # Muestra el mensaje de que el segundo número es el mayor
else: # Si no se cumple ninguna condición anterior por lo tanto el tercero es el mayor
    print("El tercer número es el mayor de los tres") # Muestra el mensaje de que el tercer número es el mayor

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 13/01/2026 
# Hora: 9:46
