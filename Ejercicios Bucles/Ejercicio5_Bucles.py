#Descripción: Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión. 
# Entrada: Una cantidad a invertir, el interés anual y el número de años
# Salida: El capital obtenido en la inversión cada año que dura la inversión

invertir = float(input("Introduzca una cantidad a invertir: ")) # Pide al usuario una cantidad a invertir
interes = float(input("Introduzca el interés anual: ")) # Pide al usuario el interés anual
años = int(input("Introduzca el número de años: ")) # Pide al usuario el número de años

for i in range(años): # Recorre todos los años dados por el usuario
    invertir += invertir * round (interes / 100, 2) # Calcula el capital obtenido en la inversión en la cantidad de años dados por el usuario 
                                                    # y lo redondea a 2 decimales (Función round)
    print("Capital obtenido en el año", i+1, ":", round(invertir, 2)) # Muestra el capital obtenido en la inversión en la cantidad de años dados por el usuario
                                                                      # y lo redondea a 2 decimales (Función round)

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 15/01/2026 
# Hora: 08:59
