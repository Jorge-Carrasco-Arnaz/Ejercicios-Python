# Descripción: Escribir una función que reciba una muestra de números 
# en una lista y devuelva un diccionario con su media, varianza y desviación
# Entrada: Nada
# Salida: Media, varianza y desviación típica

def estadisticas(lista):
    media = sum(lista) / len(lista)

    suma_cuadrados = 0
    for x in lista:
        diferencia = x - media
        suma_cuadrados += diferencia ** 2

    varianza = suma_cuadrados / len(lista)

    desviacion = varianza ** 0.5

    return {"media": media, "varianza": varianza, "desviacion": desviacion}

numeros = [9.88,9.2,2.34,1.5,2.5,2.09]

print(estadisticas(numeros))