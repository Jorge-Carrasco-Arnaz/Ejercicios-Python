import os # Importamos la librería "os" para poder limpiar la terminal cada vez que reiniciamos el menú

def borrar_pantalla(): # Función para limpiar la pantalla tras cada opción
    os.system("clear") # Limpia la pantalla introduciendo el comando "clear" en el terminal

def mostrar_contactos(): # Función para mostrar los contactos
    for nombre, telefono in agenda.items(): # Recorre el diccionario "agenda" y muestra los contactos
        print(nombre,":", telefono) # Imprime el nombre y teléfono 

def agregar_contacto(): # Función para agregar contactos

    nombre = input("Nombre: ") # Pide al usuario introducir el nombre del contacto que quiere añadir

    if nombre in agenda: # Comprueba si el nombre del contacto está en la agenda
        print("El contatcto:",nombre, "ya se encuentra en la agenda") # Imprime un mensaje de que el contacto ya se encuentra en la agenda
    else: # Si el nombre del contacto no está en la agenda
        telefono = input("Teléfono: ")  # Pide al usuario introducir el Teléfono del contacto que quiere añadir
        agenda[nombre] = telefono # Establece que el teléfono pertenece al nombre del contacto
        print("El contatcto:",nombre, "se ha añadido a la agenda.") # Imprime un mensaje de que se ha añadido el contacto

def buscar_contacto(): # Función para buscar contactos

    nombre = input("Nombre: ") # Pide al usuario introducir el nombre del contacto que quiere buscar

    if nombre in agenda: # Comprueba si el nombre del contacto está en la agenda
        print("El contacto:", nombre, "tiene el número:",agenda[nombre]) # Imprime el nombre y teléfono del contacto que se ha buscado
    else: # Si el nombre del contacto no está en la agenda
        print("El contacto:", nombre, "no se encuentra en la agenda") # Imprime un mensaje de que el contacto no se encuentra en la agenda

def eliminar_contacto(): # Función para eliminar contactos

    nombre = input("Nombre: ") # Pide al usuario introducir el nombre del contacto que quiere eliminar

    if nombre in agenda: # Comprueba si el nombre del contacto está en la agenda
        del agenda[nombre] # Elimina el contacto de la agenda
        print("El contacto:",nombre, "se ha eliminado de la agenda.") # Imprime un mensaje de que se ha eliminado el contacto
    else: # Si el nombre del contacto no está en la agenda
        print("El contacto:",nombre, "no se encuentra en la agenda.") # Imprime un mensaje de que el contacto no se encuentra en la agenda

# Diccionario con 10 párametros para el funcionamiento del programa
agenda = { "Juan Pérez": 612458932,
    "María García": 655321098,
    "Carlos López": 642118743,
    "Ana Martínez": 600342115,
    "Luis Rodríguez": 622908431,
    "Elena Sánchez": 687442309,
    "Roberto Gómez": 633112254,
    "Lucía Díaz": 699003421,
    "Fernando Ruiz": 670554432,
    "Sofía Hernández": 611887722
}
while True: # Mantiene el bucle siempre activo hasta que se encuentre con un break
    borrar_pantalla() # Llama a la función para limpiar la terminal

    # Imprime el menú de opciones
    print("=== AGENDA ===")
    print("1. Mostrar contactos")
    print("2. Agregar contacto")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    print("==============")
    
    opcion = input("Elige una opción: ") # Pide al usuario introducir una opción
   
    match opcion: # Comprobamos la opción con match(igual a switch)
        case "1": # Caso en que se introduce "1": muestra la agenda
            borrar_pantalla() # Llama a la función borrar_pantalla() para limpiar la terminal
            print("=== CONTACTOS ===") # Imprime el título del menú
            mostrar_contactos() # Llama a la función para listar el diccionario
            input("Pulsa Enter para continuar ") # Pide al usuario pulsar Enter para continuar

        case "2": # Caso en que se introduce "2": agrega un contacto
            borrar_pantalla() # Llama a la función borrar_pantalla() para limpiar la terminal
            print("=== AGREGAR CONTACTO ===") # Imprime el título del menú
            agregar_contacto() # Llama a la función para insertar nueva llave-valor
            input("Pulsa Enter para continuar ") # Pide al usuario pulsar Enter para continuar

        case "3": # Caso en que se introduce "3": busca un contacto
            borrar_pantalla() # Llama a la función borrar_pantalla() para limpiar la terminal
            print("=== BUSCAR CONTACTO ===") # Imprime el título del menú
            buscar_contacto() # Llama a la función buscar_contacto() para consultar la llave
            input("Pulsa Enter para continuar ") # Pide al usuario pulsar Enter para continuar

        case "4": # Caso en que se introduce "4": elimina un contacto
            borrar_pantalla() # Llama a la función borrar_pantalla() para limpiar la terminal
            print("=== ELIMINAR CONTACTO ===") # Imprime el título del menú
            eliminar_contacto() # Llama a la función eliminar_contacto() para borrar la llave del diccionario
            input("Pulsa Enter para continuar ") # Pide al usuario pulsar Enter para continuar

        case "5": # Caso en que se introduce "5": sale del programa
            print("Saliendo de la agenda") # Imprime un mensaje de despedida
            break # Rompe el bucle while para finalizar la ejecución

        case _: # Caso por defecto: se ejecuta si no coincide con ninguna opción anterior
            print("Parámetro no válido") # Indica que la entrada no está en el menú
            input("Pulsa Enter para reintentar ") # Pide al usuario pulsar Enter para continuar

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 21/01/2026
# Hora: 12:03