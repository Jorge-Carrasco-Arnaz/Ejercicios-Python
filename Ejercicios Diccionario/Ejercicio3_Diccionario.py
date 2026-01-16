# Descripcion: Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos 
# y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario 
# debe mostrar un mensaje informando de ello. Fruta Precio Plátano 1.35 Manzana 0.80 Pera 0.85 Naranja 0.70
# Entrada: Nombre de la fruta y número de kilos
# Salida: Precio de la fruta

frutas = {"plátano": 1.35, "manzana": 0.80, "pera": 0.85, "naranja": 0.70} # Diccionario con los precios de las frutas
fruta = input("Introduzca el nombre de la fruta: ").lower() # Pide al usuario el nombre de la fruta 
                                                            #(lo pongo en minúsculas para que no haya error por si el usuario introduce mayúsculas o minúsculas)

if fruta in frutas: # Comprueba si la fruta está en el diccionario
    kilos = float(input("Introduzca el número de kilos: ")) # Pide al usuario el número de kilos
    print("El precio de", kilos, "kilos de", fruta, "es", frutas[fruta] * kilos) # Imprime el precio de la fruta
else: # Si la fruta no está en el diccionario
    print("La fruta", fruta, "no está en el diccionario") # Imprime mensaje de error

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 16/01/2026
# Hora: 13:38
