# Descripción: Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. 
# Considerar el caso en que ambos números son iguales. 
# Entrada: Dos números dados por el usuario
# Salida: Mensaje indicando cuál de los dos números es menor

n1 = int(input("Introduce el primer número: ")) # Pide al usuario el primer número
n2 = int(input("Introduce el segundo número: ")) # Pide al usuario el segundo número

if n1 < n2: # Comprueba si el número 1 es menor que el número 2
    print("El número 1 es menor") # Imprime mensaje de que el número 1 es menor
elif n1 > n2: # Si el número 1 es mayor que el número 2
    print("El número 2 es menor") # Imprime mensaje de que el número 2 es menor
else: # Si los números son iguales
    print("Los números son iguales") # Imprime mensaje de que los números son iguales   


# Realizado por: Jorge Carrasco Arnaz
# Fecha: 13/01/2026 
# Hora: 9:26