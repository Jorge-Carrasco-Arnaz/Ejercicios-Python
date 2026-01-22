#!/bin/bash

###############################################################################
# Tarea: Monitorización de espacio en disco
# Requisito: Log estático para permitir rotación y purga profesional
###############################################################################

# --- VARIABLES (Rutas absolutas) ---
UMBRAL=80
LOG_DIR="/var/log/mantenimiento"
# El nombre del archivo es fijo para que el sistema de rotación lo reconozca
LOG_FILE="$LOG_DIR/monitorizacion_disco.log"
PARTICION="/"

# --- FUNCIONES ---

# Función de log con fecha interna (Obligatorio para diagnóstico)
log_msg() {
    # El timestamp va DENTRO del archivo, no en el nombre del archivo
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

error_exit() {
    log_msg "ERROR CRÍTICO: $1"
    exit 1
}

check_disk() {
    # 1. Preparación del entorno
    [ -d "$LOG_DIR" ] || mkdir -p "$LOG_DIR" || { echo "Error fatal: No existe $LOG_DIR"; exit 1; }

    log_msg "===== INICIO DE MONITORIZACIÓN ====="

    # 2. Obtención de datos técnica
    # Extraemos el porcentaje de uso de la partición raíz
    uso=$(df "$PARTICION" | tail -1 | awk '{print $5}' | sed 's/%//')

    # Validar que la salida sea numérica para evitar fallos de ejecución
    if [[ ! "$uso" =~ ^[0-9]+$ ]]; then
        error_exit "Error al obtener métricas de $PARTICION"
    fi

    # 3. Evaluación y Registro
    if [ "$uso" -gt "$UMBRAL" ]; then
        log_msg "ALERTA: Espacio insuficiente. Uso al $uso% (Umbral: $UMBRAL%)"
    else
        log_msg "Estado OK: Uso actual al $uso%"
    fi

    log_msg "===== FIN DE TAREA ====="
}

# --- EJECUCIÓN ---
check_disk
