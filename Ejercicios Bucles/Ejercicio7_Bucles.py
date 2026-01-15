# Descripción: Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta
# Entrada: Una contraseña dada por el usuario
# Salida: Indicar si la contraseña introducida es correcta o incorrecta

contrasenha = "contraseña" # Almacena la contraseña correcta en una variable

while True: # Bucle infinito que se repite hasta que la contraseña introducida sea correcta (Se comprueba que es correcta usando el break dentro del if)
    contrasenha_usuario = input("Introduzca la contraseña: ") # Pide al usuario que introduzca una contraseña
    if contrasenha_usuario == contrasenha: # Comprueba si la contraseña introducida es correcta
        print("Muy bien chaval la has clavado, venga entra a hackearme 🎉") # Muestra un mensaje indicando que la contraseña introducida es correcta
        break # Sale del bucle
    else: # Si la contraseña introducida no es correcta
        print("Me da a mi que esa no va a ser 🤣") # Muestra un mensaje indicando que la contraseña introducida es incorrecta

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 15/01/2026 
# Hora: 09:14
