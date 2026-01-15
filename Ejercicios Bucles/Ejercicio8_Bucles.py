# Descripción: Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase. 
# Entrada: Una frase y una letra dadas por el usuario
# Salida: Número de veces que aparece la letra en la frase

frase = str(input("Introduzca una frase: ")) # Pide al usuario una frase
letra = str(input("Introduzca una letra: ")) # Pide al usuario una letra

c = 0 # Inicializamos la variable que hará de contador

for i in frase: # Recorre la frase carácter por carácter
    if i == letra: # Si el carácter coincide con la letra introducida
        c += 1  # Si el carácter coincide, sumamos 1 al contador

print("La letra " ,letra, " aparece " ,c, " veces en la frase") # Muestra el número de veces que aparece la letra en la frase

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 15/01/2026 
# Hora: 09:36
