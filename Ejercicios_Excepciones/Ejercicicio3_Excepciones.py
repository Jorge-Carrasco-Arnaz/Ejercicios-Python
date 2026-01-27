# Descripción: Crear una función que recorra una lista desde 0 hasta su longitud+1.
# En el programa principal definir una lista y se llama a la función. Se debe controlar la excepción IndexError.
# Entrada: Una lista
# Salida: Recorrer la lista o un mensaje de error si se produce un IndexError

def recorrer_lista(lista): # Función que recorre una lista
    try: # Intenta recorrer la lista
        for i in range(len(lista) + 1): # Recorre la lista desde 0 hasta su longitud+1
            print(lista[i]) # Imprime el elemento de la lista
    except IndexError: # Si se produce un error al recorrer la lista, devuelve un mensaje de error
        print("Error: Picha que no puedes recorrer la lista 😵💫") # Mensaje de error

lista = [1, 2, 3, 6] # Lista de números

recorrer_lista(lista) # Llama a la función

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 27/01/2026
# Hora: 11:00
