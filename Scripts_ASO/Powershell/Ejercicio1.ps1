<#
.SYNOPSIS
    Ejercicio 1: Script profesional de limpieza de archivos temporales.
    Cumple con estándares de modularidad, trazabilidad y seguridad.
#>

# --- FUNCIÓN DE LOG (Modular y Reutilizable) ---
function Write-ProfessionalLog {
    param (
        [Parameter(Mandatory = $true)] [string]$Message,
        [Parameter(Mandatory = $true)] [string]$LogPath  # Este es el nombre del parámetro
    )
    # Generación de timestamp obligatorio para diagnóstico
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $Line = "[$Timestamp] $Message"
    
    try {
        # Asegurar que el directorio del log existe (Evita fallos de entorno)
        $LogDir = Split-Path $LogPath
        if (-not (Test-Path $LogDir)) { 
            New-Item -ItemType Directory -Path $LogDir -Force | Out-Null 
        }
        # Escritura con log estático y contenido dinámico
        Add-Content -Path $LogPath -Value $Line -Encoding utf8
    }
    catch {
        # Salida controlada ante fallos de permisos
        Write-Error "Fallo crítico escribiendo en log: $($_.Exception.Message)"
        exit 1
    }
}

# --- FUNCIÓN DE LIMPIEZA ---
function Start-LimpiezaTemporales {
    param (
        [string]$RutaTarget = "C:\Windows\Temp",
        [int]$DiasRetencion = 7,
        [string]$LogFile = "C:\Logs\Mantenimiento_Sistemas.log" # Log estático
    )

    # Registro de inicio (Evidencia de ejecución)
    Write-ProfessionalLog -Message "INICIO: Proceso de limpieza en $RutaTarget" -LogPath $LogFile

    try {
        # 1. Comprobación de existencia del origen (Ruta absoluta)
        if (-not (Test-Path $RutaTarget)) {
            throw "El directorio origen no existe: $RutaTarget"
        }

        # 2. Cálculo de fecha y búsqueda de archivos
        $FechaCorte = (Get-Date).AddDays(-$DiasRetencion)
        $Archivos = Get-ChildItem -Path $RutaTarget -File -ErrorAction Stop | 
                    Where-Object { $_.LastWriteTime -lt $FechaCorte }
        
        $Contador = ($Archivos | Measure-Object).Count

        # 3. Ejecución del borrado con control de errores
        if ($Contador -gt 0) {
            Write-ProfessionalLog -Message "Borrando $Contador archivos con más de $DiasRetencion días..." -LogPath $LogFile
            $Archivos | Remove-Item -Force -ErrorAction Stop
            Write-ProfessionalLog -Message "ÉXITO: Se han eliminado $Contador archivos." -LogPath $LogFile
        } else {
            Write-ProfessionalLog -Message "No se encontraron archivos antiguos para eliminar." -LogPath $LogFile
        }
    }
    catch {
        # Captura de error para diagnóstico profesional
        Write-ProfessionalLog -Message "ERROR: $($_.Exception.Message)" -LogPath $LogFile
        exit 1
    }
    finally {
        # Cierre de tarea (Trazabilidad)
        Write-ProfessionalLog -Message "FIN: Tarea finalizada." -LogPath $LogFile
    }
}

# --- EJECUCIÓN ---
# Invocación con rutas absolutas para garantizar éxito en Task Scheduler [cite: 485, 525]
Start-LimpiezaTemporales -RutaTarget "C:\Windows\Temp" -DiasRetencion 7 -LogFile "C:\Logs\Ejercicio1.log"
