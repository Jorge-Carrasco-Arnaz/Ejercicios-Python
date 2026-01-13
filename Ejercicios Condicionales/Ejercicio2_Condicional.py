# Descripción: Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. 
# No considerar el caso en que ambos números son iguales.
# Entrada: Dos números dados por el usuario
# Salida: Mensaje indicando cuál de los dos números es menor

n1 = int(input("Introduce el primer número: ")) # Pide al usuario el primer número
n2 = int(input("Introduce el segundo número: ")) # Pide al usuario el segundo número

if n1 < n2: # Comprueba si el número 1 es menor que el número 2
    print("El número 1 es menor") # Imprime mensaje de que el número 1 es menor
else: # Si no es menor
    print("El número 2 es menor") # Imprime mensaje de que el número 2 es menor

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 12/01/2026 
# Hora: 13:01

