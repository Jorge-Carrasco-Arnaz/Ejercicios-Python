import pymysql # Importa la libreria pymysql para la conexion con la base de datos
import os # Importa la libreria os para gestionar comandos del sistema operativo

# Configuracion de los parametros de acceso a la base de datos local
HOST = "localhost" # Define la direccion del servidor local
PORT = 3306 # Define el puerto estandar de MariaDB
USER = "root" # Define el usuario administrador para la conexion
PASSWORD = "root" # Define la contraseña establecida tras la reinstalacion
DATABASE = "agenda_db" # Define el nombre de la base de datos agenda_db

def borrar_pantalla(): # Funcion para limpiar la terminal tras cada opcion
    if os.name == 'posix': # Comprueba si el sistema es Linux o Unix
        os.system('clear') # Ejecuta el comando clear para limpiar la terminal
    else: # Si el sistema operativo es Windows
        os.system('cls') # Ejecuta el comando cls para limpiar la terminal

def mostrar_contactos(conn): # Funcion para mostrar los contactos desde la base de datos
    borrar_pantalla() # Llama a la funcion para limpiar la pantalla
    mi_cursor = conn.cursor() # Crea un cursor para ejecutar sentencias SQL
    mi_cursor.execute("SELECT * FROM contactos") # Ejecuta la consulta de seleccion
    resultados = mi_cursor.fetchall() # Obtiene todos los registros devueltos
    
    print("=== LISTA DE CONTACTOS ===") # Imprime el encabezado del listado
    for fila in resultados: # Recorre cada registro obtenido de la base de datos
        print(f"ID: {fila[0]} | Nombre: {fila[1]} | Teléfono: {fila[2]}") # Muestra los datos
    
    input("\nPulsa Enter para continuar...") # Pausa la ejecucion para el usuario

def agregar_contacto(conn): # Funcion para insertar un nuevo contacto en la tabla
    borrar_pantalla() # Limpia la pantalla de la terminal
    print("=== AGREGAR CONTACTO ===") # Imprime el encabezado de la opcion
    nombre = input("Nombre: ") # Pide al usuario el nombre del nuevo contacto
    telefono = input("Teléfono: ") # Pide al usuario el telefono del nuevo contacto
    
    mi_cursor = conn.cursor() # Crea un cursor para la operacion SQL
    sql = "INSERT INTO contactos (nombre, telefono) VALUES (%s, %s)" # Define la sentencia SQL
    mi_cursor.execute(sql, (nombre, telefono)) # Ejecuta la insercion con los datos
    conn.commit() # Confirma los cambios de forma permanente en la base de datos
    print(f"El contacto {nombre} se ha añadido correctamente.") # Informa del exito
    input("Pulsa Enter para continuar...") # Pausa la ejecucion

def buscar_contacto(conn): # Funcion para buscar un contacto por su nombre
    borrar_pantalla() # Limpia la pantalla de la terminal
    print("=== BUSCAR CONTACTO ===") # Imprime el encabezado de la opcion
    nombre = input("Nombre a buscar: ") # Pide el nombre que se quiere consultar
    
    mi_cursor = conn.cursor() # Crea un cursor para la consulta SQL
    sql = "SELECT * FROM contactos WHERE nombre = %s" # Define la consulta con filtro
    mi_cursor.execute(sql, (nombre,)) # Ejecuta la busqueda filtrada
    resultado = mi_cursor.fetchone() # Obtiene el primer resultado encontrado
    
    if resultado: # Comprueba si se encontro el contacto en la tabla
        print(f"Contacto encontrado: {resultado[1]} | Teléfono: {resultado[2]}") # Muestra datos
    else: # Si la consulta no devuelve ningun registro
        print("El contacto no se encuentra en la agenda.") # Informa al usuario
    input("Pulsa Enter para continuar...") # Pausa la ejecucion

def eliminar_contacto(conn): # Funcion para borrar un contacto de la base de datos
    borrar_pantalla() # Limpia la pantalla de la terminal
    print("=== ELIMINAR CONTACTO ===") # Imprime el encabezado de la opcion
    nombre = input("Nombre del contacto a eliminar: ") # Pide el nombre a borrar
    
    mi_cursor = conn.cursor() # Crea un cursor para la operacion SQL
    sql = "DELETE FROM contactos WHERE nombre = %s" # Define la sentencia de borrado
    mi_cursor.execute(sql, (nombre,)) # Ejecuta el borrado filtrando por nombre
    conn.commit() # Aplica los cambios en la base de datos permanentemente
    
    if mi_cursor.rowcount > 0: # Comprueba si se ha eliminado alguna fila realmente
        print(f"El contacto {nombre} ha sido eliminado.") # Informa del exito
    else: # Si no se elimino ninguna fila del sistema
        print("No se encontró ningún contacto con ese nombre.") # Informa del fallo
    input("Pulsa Enter para continuar...") # Pausa la ejecucion

def menu(): # Funcion principal que gestiona el flujo del programa
    try: # Inicia bloque para gestionar la conexion inicial
        # Establece la conexion con MariaDB usando los parametros definidos
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, database=DATABASE)
        
        while True: # Mantiene el menu activo en un bucle infinito
            borrar_pantalla() # Limpia la terminal antes de mostrar el menu
            print("\n=== MENÚ APP AGENDA ===") # Encabezado principal del menu
            print("1. Mostrar contactos") # Opcion para listar registros
            print("2. Agregar contacto") # Opcion para insertar registros
            print("3. Buscar contacto") # Opcion para buscar registros
            print("4. Eliminar contacto") # Opcion para borrar registros
            print("5. Salir") # Opcion para cerrar el programa
            
            opcion = input("Elige una opción: ") # Recoge la seleccion del usuario
            
            if opcion == "1": # Caso mostrar contactos
                mostrar_contactos(conn) # Llama a la funcion de listar
            elif opcion == "2": # Caso agregar contacto
                agregar_contacto(conn) # Llama a la funcion de insercion
            elif opcion == "3": # Caso buscar contacto
                buscar_contacto(conn) # Llama a la funcion de busqueda
            elif opcion == "4": # Caso eliminar contacto
                eliminar_contacto(conn) # Llama a la funcion de borrado
            elif opcion == "5": # Caso salir del programa
                print("Saliendo de la aplicación...") # Mensaje de despedida
                conn.close() # Cierra la conexion de forma segura con la DB
                break # Rompe el bucle para terminar la ejecucion
    except pymysql.MySQLError as e: # Captura errores generales de conexion
        print(f"Error crítico de conexión: {e}") # Muestra el fallo grave

if __name__ == "__main__": # Verifica si el script se ejecuta directamente
    menu() # Llama a la funcion menu para iniciar la aplicacion

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 10/02/2026