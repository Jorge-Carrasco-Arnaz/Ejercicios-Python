import pymysql # Importa la libreria pymysql para la conexion

# 1. Configuracion de la conexion a la base de datos local
try: # Inicia el bloque de prueba para capturar errores
    conexion = pymysql.connect( # Define los parametros de la conexion
        host="localhost", # Define el host como servidor local
        port=3306, # Define el puerto estandar de MariaDB
        user="root", # Define el usuario administrador root
        password="root", # Define la contraseña de acceso
        database="db_Jorge" # Define la base de datos db_Jorge
    )

    # 2. Crear un cursor para poder ejecutar las consultas SQL
    mi_cursor = conexion.cursor() # Crea el objeto cursor para interactuar

    # 3. Ejecutar la consulta para obtener los datos de la tabla
    mi_cursor.execute("SELECT * FROM contactos") # Ejecuta el comando SELECT

    # 4. Obtener y mostrar los resultados por pantalla
    resultados = mi_cursor.fetchall() # Recupera todos los registros encontrados

    for fila in resultados: # Inicia el bucle para recorrer cada registro
        print(f"DNI: {fila[0]} | Nombre: {fila[1]}") # Imprime los campos de cada fila

# 5. Asegurar el cierre de la conexion al finalizar
finally: # Bloque que se ejecuta siempre al terminar
    if 'conexion' in locals(): # Comprueba si la conexion se llego a crear
        mi_cursor.close() # Cierra el cursor de forma segura
        conexion.close() # Cierra la conexion con el servidor
        print("Conexion cerrada correctamente.") # Imprime confirmacion de cierre

# Realizado por: Jorge Carrasco Arnaz
# Fecha: 10/02/2026