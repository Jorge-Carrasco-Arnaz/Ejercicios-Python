import pymysql # Importa la libreria pymysql para la conexion con la base de datos
import os # Importa la libreria os para gestionar comandos del sistema operativo

# Definicion de los parametros de conexion segun los requisitos del ejercicio
HOST = "localhost" # Define la direccion del servidor local
PORT = 3306 # Define el puerto estandar de MariaDB
USER = "root" # Define el usuario administrador para la conexion
PASSWORD = "root" # Define la contraseña establecida tras la reinstalacion
DATABASE = "agenda_db" # Define el nombre de la base de datos agenda_db

def borrar_pantalla(): # Funcion para limpiar la terminal tras cada opcion
    os.system('clear') # Usa el comando clear para limpiar la terminal


def mostrar_contactos(conn): # Funcion para mostrar los contactos desde la base de datos
    borrar_pantalla() # Llama a la funcion para limpiar la pantalla
    mi_cursor = conn.cursor() # Crea un cursor para ejecutar sentencias SQL
    mi_cursor.execute("SELECT * FROM contactos") # Ejecuta la consulta de seleccion
    resultados = mi_cursor.fetchall() # Obtiene todos los registros devueltos
    
    print("=== LISTA DE CONTACTOS ===") # Imprime el encabezado del listado
    for fila in resultados: # Recorre cada registro obtenido de la base de datos
        print(f"ID: {fila[0]} | Nombre: {fila[1]} | Teléfono: {fila[2]}") # Muestra los datos por consola
    
    input("\nPulsa Enter para continuar...") # Pausa la ejecucion para el usuario

def agregar_contacto(conn): # Funcion para insertar un nuevo contacto en la tabla
    borrar_pantalla() # Limpia la pantalla de la terminal
    print("=== AGREGAR CONTACTO ===") # Imprime el encabezado de la opcion
    nombre = input("Nombre: ") # Pide al usuario el nombre del nuevo contacto
    telefono = input("Teléfono: ") # Pide al usuario el telefono del nuevo contacto
    
    mi_cursor = conn.cursor() # Crea un cursor para la operacion SQL
    sql = "INSERT INTO contactos (nombre, telefono) VALUES (%s, %s)" # Define la sentencia SQL de insercion
    mi_cursor.execute(sql, (nombre, telefono)) # Ejecuta la insercion con los datos proporcionados
    conn.commit() # Confirma los cambios de forma permanente en la base de datos
    print(f"El contacto {nombre} se ha añadido correctamente.") # Imprime mensaje de éxito
    input("Pulsa Enter para continuar...") # Pausa la ejecucion

def buscar_contacto(conn): # Funcion para buscar un contacto por su nombre
    borrar_pantalla() # Limpia la pantalla de la terminal
    print("=== BUSCAR CONTACTO ===") # Imprime el encabezado de la opcion
    nombre = input("Nombre a buscar: ") # Pide el nombre que se quiere consultar
    
    mi_cursor = conn.cursor() # Crea un cursor para la consulta SQL
    sql = "SELECT * FROM contactos WHERE nombre = %s" # Define la consulta con filtro de busqueda
    mi_cursor.execute(sql, (nombre,)) # Ejecuta la busqueda filtrada en la base de datos
    resultado = mi_cursor.fetchone() # Obtiene el primer resultado encontrado
    
    if resultado: # Comprueba si se encontro el contacto en la tabla
        print(f"Contacto encontrado: {resultado[1]} | Teléfono: {resultado[2]}") # Muestra los datos encontrados
    else: # Si la consulta no devuelve ningun registro
        print("El contacto no se encuentra en la agenda.") # Imprime mensaje de error
    input("Pulsa Enter para continuar...") # Pausa la ejecucion

def eliminar_contacto(conn): # Funcion para borrar un contacto de la base de datos
    borrar_pantalla() # Limpia la pantalla de la terminal
    print("=== ELIMINAR CONTACTO ===") # Imprime el encabezado de la opcion
    nombre = input("Nombre del contacto a eliminar: ") # Pide el nombre del contacto a borrar
    
    mi_cursor = conn.cursor() # Crea un cursor para la operacion SQL
    sql = "DELETE FROM contactos WHERE nombre = %s" # Define la sentencia SQL de borrado
    mi_cursor.execute(sql, (nombre,)) # Ejecuta el borrado filtrando por nombre
    conn.commit() # Aplica los cambios en la base de datos de forma permanente
    
    if mi_cursor.rowcount > 0: # Comprueba si se ha eliminado alguna fila realmente
        print(f"El contacto {nombre} ha sido eliminado.") # Imprime mensaje de éxito
    else: # Si no se ha podido eliminar ninguna fila del sistema
        print("No se encontró ningún contacto con ese nombre.") # Imprime mensaje de fallo
    input("Pulsa Enter para continuar...") # Pausa la ejecucion


# Establece la conexion inicial con MariaDB
conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, database=DATABASE)
    
while True: # Mantiene el menu activo en un bucle infinito hasta que se solicite salir
    borrar_pantalla() # Limpia la terminal antes de mostrar las opciones del menu
    print("\n=== MENÚ APP AGENDA ===") # Imprime el encabezado principal del menu
    print("1. Mostrar contactos") # Muestra la opcion para listar registros
    print("2. Agregar contacto") # Muestra la opcion para insertar nuevos registros
    print("3. Buscar contacto") # Muestra la opcion para realizar busquedas
    print("4. Eliminar contacto") # Muestra la opcion para borrar registros
    print("5. Salir") # Muestra la opcion para finalizar el programa
        
    opcion = input("Elige una opción: ") # Recoge la seleccion del usuario por teclado
        
    if opcion == "1": # Comprueba si el usuario eligio la opcion 1
        mostrar_contactos(conn) # Llama a la funcion encargada de listar contactos
    elif opcion == "2": # Comprueba si el usuario eligio la opcion 2
        agregar_contacto(conn) # Llama a la funcion encargada de insertar contactos
    elif opcion == "3": # Comprueba si el usuario eligio la opcion 3
        buscar_contacto(conn) # Llama a la funcion encargada de buscar contactos
    elif opcion == "4": # Comprueba si el usuario eligio la opcion 4
        eliminar_contacto(conn) # Llama a la funcion encargada de borrar contactos
    elif opcion == "5": # Comprueba si el usuario eligio la opcion 5 de salida
        print("Saliendo de la aplicación...") # Muestra un mensaje de despedida
        conn.close() # Cierra la conexion con la base de datos de forma segura
        break # Rompe el bucle while para finalizar la ejecucion del script
    else: # En caso de que la entrada no coincida con ninguna opcion valida
            print("Opción no válida. Inténtalo de nuevo.") # Informa al usuario del error
            input("Pulsa Enter para reintentar") # Pausa la ejecucion antes de volver al menu


# Realizado por: Jorge Carrasco Arnaz
# Fecha: 11/02/2026