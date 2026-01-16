# Descripción: Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$',
# 'Yen':'Y'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de
# aviso si la divisa no está en el diccionario.
# Entrada: Consulta de la moneda que quiere consultar el usuario
# Salida: Imprime mensaje del símbolo de la moneda

Monedas = { "Euro" : "€" , "Dollar" :"$", "Yen" :"Y" } # Diccionario con las monedas y sus símbolos

Consulta = str(input("Introduzca la moneda que quiere consultar: ")) # Pide al usuario la moneda que quiere consultar

if Consulta in Monedas: # Comprueba si la moneda está en el diccionario
    print("El símbolo de la moneda es:",Monedas.get(Consulta)) # Imprime el símbolo de la moneda
else: # Si no está en el diccionario
    print("La moneda no está en el diccionario") # Imprime mensaje de error

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 16/01/2026
# Hora: 13:13
