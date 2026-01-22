#!/bin/bash

###############################################################################
# Tarea: Copia de seguridad profesional con versionado
# Requisitos: No sobrescribir, verificar integridad y usar log estático
###############################################################################

# --- VARIABLES (Rutas absolutas) ---
ORIGEN="/home/usuario/Documentos"
DESTINO_BASE="/backups/documentos"
# Nombre de log estático para facilitar la rotación del sistema
LOG_FILE="/var/log/mantenimiento/Ejercicio3.log"

# Variable para el nombre del archivo (incluye fecha para el versionado)
FECHA_VERSION=$(date +"%Y-%m-%d_%H%M")
BACKUP_FILE="backup_doc_$FECHA_VERSION.tar.gz"

# --- FUNCIONES ---

# Registro con fecha interna para diagnóstico y auditoría
log_msg() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

# Salida controlada en caso de fallo crítico
error_exit() {
    log_msg "ERROR: $1"
    exit 1
}

backup_profesional() {
    # 1. Preparación del entorno
    # Crear carpeta de logs si no existe
    [ -d "/var/log/mantenimiento" ] || mkdir -p "/var/log/mantenimiento"
    
    log_msg "===== INICIO DE BACKUP VERSIONADO ====="

    # Comprobar si el origen existe
    if [ ! -d "$ORIGEN" ]; then
        error_exit "El directorio origen no existe: $ORIGEN"
    fi

    # Asegurar que el destino existe
    mkdir -p "$DESTINO_BASE" || error_exit "No se pudo crear el directorio de destino"

    # 2. Ejecución: Compresión y empaquetado (Versionado real)
    log_msg "Creando archivo de respaldo: $BACKUP_FILE"
    
    # tar es preferible a cp porque preserva permisos y comprime
    tar -czf "$DESTINO_BASE/$BACKUP_FILE" "$ORIGEN" 2>> "$LOG_FILE"

    if [ $? -ne 0 ]; then
        error_exit "El comando tar falló durante la ejecución."
    fi

    # 3. Verificación (No es que el comando termine, es que el archivo sirva)
    # Comprobar si el archivo existe y no está vacío
    if [ -s "$DESTINO_BASE/$BACKUP_FILE" ]; then
        log_msg "VERIFICACIÓN: El archivo se ha creado y tiene tamaño correcto."
    else
        error_exit "VERIFICACIÓN FALLIDA: El backup generado está vacío."
    fi

    log_msg "===== FIN DE TAREA: BACKUP COMPLETADO ====="
}

# --- EJECUCIÓN ---
backup_profesional
