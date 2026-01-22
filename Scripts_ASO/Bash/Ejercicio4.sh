#!/bin/bash

###############################################################################
# Tarea: Rotación y Purga de Logs (Mantenimiento)
# Objetivo: Evitar saturación de disco y mantener historial controlado
###############################################################################

# --- VARIABLES (Rutas absolutas y nombres estáticos) ---
TARGET_DIR="/var/log" # Ejemplo de subdirectorio controlado
RETENCION_COMPRIMIR=7
RETENCION_BORRAR=30
LOG_MANTENIMIENTO="/var/log/mantenimiento/Ejercicio4.log"

# --- FUNCIONES ---

# Registro con timestamp en cada línea (Evidencia y Auditoría)
log_msg() {
    # El log es estático, el contenido dinámico con fecha interna
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_MANTENIMIENTO"
}

error_exit() {
    log_msg "ERROR: $1"
    exit 1
}

gestionar_mantenimiento() {
    # 1. Asegurar entorno de logs y permisos
    [ -d "/var/log/mantenimiento" ] || mkdir -p "/var/log/mantenimiento"
    
    log_msg "===== INICIO: Tarea de Rotación y Purga ====="

    # 2. Verificación de seguridad del directorio objetivo
    if [ ! -d "$TARGET_DIR" ]; then
        error_exit "El directorio objetivo no existe o no es accesible: $TARGET_DIR"
    fi

    # 3. Rotación (Compresión): Crea nuevos logs y conserva antiguos periódicamente
    log_msg "Comprimiendo logs con más de $RETENCION_COMPRIMIR días..."
    count_gzip=$(find "$TARGET_DIR" -name "*.log" -mtime +$RETENCION_COMPRIMIR | wc -l)
    
    # Ejecución sin silenciar errores (redirección al log de mantenimiento)
    find "$TARGET_DIR" -name "*.log" -mtime +$RETENCION_COMPRIMIR -exec gzip {} \; 2>> "$LOG_MANTENIMIENTO"
    
    if [ $? -eq 0 ]; then
        log_msg "Compresión finalizada. Archivos procesados: $count_gzip"
    else
        log_msg "AVISO: Se detectaron errores durante la compresión."
    fi

    # 4. Purga: Elimina logs que ya no son útiles (seguridad de espacio)
    log_msg "Eliminando archivos comprimidos con más de $RETENCION_BORRAR días..."
    count_delete=$(find "$TARGET_DIR" -name "*.gz" -mtime +$RETENCION_BORRAR | wc -l)
    
    find "$TARGET_DIR" -name "*.gz" -mtime +$RETENCION_BORRAR -delete 2>> "$LOG_MANTENIMIENTO"
    
    if [ $? -eq 0 ]; then
        log_msg "Purga finalizada. Archivos eliminados: $count_delete"
    else
        log_msg "AVISO: Se detectaron errores durante la purga."
    fi

    log_msg "===== FIN DE TAREA: Mantenimiento completado ====="
}

# --- EJECUCIÓN ---
gestionar_mantenimiento
