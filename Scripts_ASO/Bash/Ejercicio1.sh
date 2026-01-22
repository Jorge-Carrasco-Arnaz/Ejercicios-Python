#!/bin/bash

# --- VARIABLES ---
# Usamos rutas absolutas para asegurar que funcione en Cron
LOG_DIR="/var/log/mantenimiento"
FECHA=$(date +"%Y-%m-%d")
LOG_FILE="$LOG_DIR/Ejercicio1$FECHA.log"
TARGET_DIR="/tmp"
RETENCION_DIAS=7

# --- FUNCIONES ---

# Función de log profesional con timestamp
log_msg() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

# Función para salida controlada ante errores críticos
error_exit() {
    log_msg "ERROR CRÍTICO: $1"
    exit 1
}

limpiar_sistema() {
    # 1. Preparación del entorno y logs
    mkdir -p "$LOG_DIR" || { echo "Error: No se pudo crear el directorio de logs"; exit 1; }
    
    log_msg "===== INICIO DE TAREA: LIMPIEZA DE TEMPORALES ====="

    # 2. Comprobaciones previas (Existencia de directorio)
    if [ ! -d "$TARGET_DIR" ]; then
        error_exit "El directorio objetivo no existe: $TARGET_DIR"
    fi

    # 3. Ejecución de la tarea con control de errores
    log_msg "Buscando archivos con más de $RETENCION_DIAS días en $TARGET_DIR..."
    
    # Contamos antes de borrar para el informe final
    num_archivos=$(find "$TARGET_DIR" -type f -mtime +$RETENCION_DIAS | wc -l)

    # Borramos y redirigimos posibles errores de permisos al log
    find "$TARGET_DIR" -type f -mtime +$RETENCION_DIAS -delete 2>> "$LOG_FILE"

    # 4. Verificación del resultado del comando anterior ($?)
    if [ $? -eq 0 ]; then
        log_msg "Tarea finalizada con éxito. Archivos eliminados: $num_archivos"
    else
        log_msg "AVISO: La tarea terminó pero se registraron errores durante el borrado."
    fi

    log_msg "===== FIN DE LA TAREA ====="
}

# Ejecución
limpiar_sistema
