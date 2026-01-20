# Descripción: Escribir una función que reciba una muestra de números y te haga la media de lista
# Entrada: Nada
# Salida: Media

def media (lista): # Definimos la función media
    total = sum(lista) # Sumamos todos elementos de la lista
    media_f = total / len(lista) # Dividimos el total entre la longitud de la lista para sacar la media
    return round(media_f , 2) # Devolvemos la media con solo 2 decimales

numeros = [9.88,9.2,2.34,1.5,2.5,2.09] # Establecemos una lista

print(media(numeros)) # Imprimimos la media


