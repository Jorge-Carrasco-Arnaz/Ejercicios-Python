# Descripción: Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después 
# debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <Teléfono> .  
# Entrada: Nombre, edad, dirección y teléfono del usuario
# Salida: Mensaje con la información del usuario

Persona = { "Nombre" : str(input("Introduzca su nombre: ")) ,       #
            "Edad" : int(input("Introduzca su edad: ")) ,           #   Diccionario de la información del usuario
            "Dirección" : str(input("Introduzca su dirección: ")) , #
            "Teléfono" : str(input("Introduzca su teléfono: ")) }   #

print(Persona.get("Nombre"),                                              #
     "tiene",Persona.get("Edad"),"años, vive en",Persona.get("Dirección") # Imprime el mensaje sobre la información del usuario
     ,"y su número de teléfono es",Persona.get("Teléfono"))               # 

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 16/01/2026
# Hora: 13:25