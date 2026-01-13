# Descripción: Solicitar al usuario un número. Si el número es el 1000, imprimir  un mensaje de ganador.
# Si el número es distinto de 1000, imprimir un mensaje de perdedor.
# Entrada: Número dado por el usuario
# Salida: Mensaje de ganador o perdedor

x = int(input("Introduce un número para tener la posibilidad de ganar un jugoso premio: ")) # Pide al usuario un número entero

if x == 1000: # Comprueba si el número es 1000
    print("Ganaste un premio") # Imprime mensaje de ganador
else: # Si no es 1000
    print("Lo siento, fallastes 😂") # Imprime mensaje de perdedor

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 12/01/2026 
# Hora: 12:55
