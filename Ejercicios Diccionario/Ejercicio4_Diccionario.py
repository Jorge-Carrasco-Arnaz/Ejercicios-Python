# Descripcion: Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por
# pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes
# Entrada: Fecha en formato dd/mm/aaaa
# Salida: Fecha en formato dd de <mes> de aaaa

meses = {1:"enero", 2:"febrero", 3:"marzo", 4:"abril", 5:"mayo", 6:"junio",                  #
        7:"julio", 8:"agosto", 9:"septiembre", 10:"octubre", 11:"noviembre", 12:"diciembre"} # Definimos el diccionario con los nombres de los meses

fecha = input("Introduzca una fecha en formato dd/mm/aaaa: ") # Pide al usuario que introduzca una fecha

fecha_completa = fecha.split("/") # Divide la cadena usando la barra "/" como separador
dia = int(fecha_completa[0]) # Extrae el día y lo convierte a entero para que no de error en el if
mes_numero = int(fecha_completa[1]) # Extrae el mes y lo convierte a entero para poder leerlo en el diccionario
anio = int(fecha_completa[2]) # Extrae el año y lo convierte a entero para que no de error en el if

if dia >= 31: # Comprueba si el dia es mayor o igual a 31
    print("El dia introducido no es valido") # Si el dia es mayor o igual a 31, imprime que no es valido
    quit() # Sale del programa
if mes_numero >= 12: # Comprueba si el mes es mayor o igual a 12 
    print("El mes introducido no es valido") # Si el mes es mayor o igual a 12, imprime que no es valido
    quit() # Sale del programa
else:
    mes_nombre = meses[mes_numero] # Obtenemos el nombre del mes

print(dia," de ",mes_nombre," de ", anio) # Imprime la fecha


# Realizado por: Jorge Carrasco Arnaz
# Fecha: 16/01/2026
# Hora: 14:08