# Descripción: Requerir al usuario que ingrese un día de la semana en minusculas e imprimir un mensaje si es lunes, 
# otro mensaje diferente si es viernes, 
# otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje. 

# Entrada: Un día de la semana en minúsculas
# Salida: Un mensaje indicando si es lunes, viernes, sábado, domingo o ninguno de los anteriores

dia = str(input("Introduzca el día de las semana, porfavor introduzcalo en minúsculas: ")) # Pide al usuario que introduzca el día de la semana en minúsculas
dia = dia.lower() # Convierte el día introducido a minúsculas (Esto no es necesario pero lo introduzco para evitar errores)

if dia == "lunes": # Comprueba si el día es lunes
    print("Hoy es lunes que pena 😭") # Imprime por pantalla el mensaje de que es lunes
elif dia == "viernes": # Comprueba si el día es viernes
    print("¡QUE LOCURA HOY ES VIERNES! 🥳") # Imprime por pantalla el mensaje de que es viernes
elif dia == "sábado" or dia == "domingo": # Comprueba si el día es sábado o domingo
    print("¡SI HOMBRE ES FINDE SEMANA 🪩!") # Imprime por pantalla el mensaje de que es finde semana
elif dia == "martes" or dia == "miércoles" or dia == "jueves": # Comprueba si el día no es ninguno de los anteriores
    print("Yo este día como que no me cuadra 😕") # Imprime por pantalla el mensaje de que el día no es ninguno de los anteriores

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 13/01/2026 
# Hora: 10:06

