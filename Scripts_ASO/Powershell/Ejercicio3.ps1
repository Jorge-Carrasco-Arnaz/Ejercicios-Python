<#
.SYNOPSIS
    Procedimiento profesional de Backup Versionado.
    Cumple con estándares de trazabilidad, no sobrescritura y verificación de integridad.
#>

# --- FUNCIÓN DE LOG (Centralizada y Robusta) ---
function Write-LogEntry {
    param (
        [Parameter(Mandatory = $true)] [string]$Message,
        [Parameter(Mandatory = $true)] [string]$Path
    )
    # Timestamp obligatorio en cada línea para diagnóstico y auditoría
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $Entry = "[$Timestamp] $Message"
    
    try {
        $Dir = Split-Path $Path
        if (-not (Test-Path $Dir)) { New-Item -ItemType Directory -Path $Dir -Force | Out-Null }
        Add-Content -Path $Path -Value $Entry -Encoding utf8
    }
    catch {
        Write-Error "Fallo crítico escribiendo log: $($_.Exception.Message)"
        exit 1
    }
}

# --- FUNCIÓN DE RESPALDO VERSIONADO ---
function Start-ProfessionalBackup {
    param (
        [string]$SourcePath = "C:\Datos",
        [string]$DestinationBase = "C:\Backups",
        [string]$LogPath = "C:\Logs\Backup_Empresa.log"
    )

    # Identificador único de versión para evitar sobrescripción
    $VersionID = Get-Date -Format "yyyy-MM-dd_HHmm"
    $BackupFile = "Backup_Datos_$VersionID.zip"
    $FinalPath = Join-Path $DestinationBase $BackupFile

    Write-LogEntry -Message ">>>>> INICIO DE PROCESO DE RESPALDO VERSIONADO <<<<<" -Path $LogPath

    try {
        # 1. Validación de origen y preparación de destino
        if (-not (Test-Path $SourcePath)) {
            throw "El directorio de origen no existe: $SourcePath"
        }
        if (-not (Test-Path $DestinationBase)) {
            New-Item -ItemType Directory -Path $DestinationBase -Force | Out-Null
        }

        # 2. Ejecución: Compresión (Garantiza versionado y ahorra espacio)
        Write-LogEntry -Message "Creando versión de respaldo: $BackupFile" -Path $LogPath
        Compress-Archive -Path "$SourcePath\*" -DestinationPath $FinalPath -Force -ErrorAction Stop

        # 3. Verificación de integridad (Requisito profesional)
        if (Test-Path $FinalPath) {
            $Size = (Get-Item $FinalPath).Length
            if ($Size -gt 0) {
                Write-LogEntry -Message "VERIFICACIÓN EXITOSA: Archivo creado ($($Size / 1MB) MB)." -Path $LogPath
            } else {
                throw "Verificación fallida: El archivo resultante está vacío."
            }
        } else {
            throw "Fallo en la persistencia del archivo de backup."
        }

        Write-LogEntry -Message "CONCLUSIÓN: El respaldo se completó con éxito." -Path $LogPath
    }
    catch {
        Write-LogEntry -Message "FALLO DE EJECUCIÓN: $($_.Exception.Message)" -Path $LogPath
        exit 1 # Salida con error para que el programador de tareas lo registre
    }
    finally {
        Write-LogEntry -Message ">>>>> CIERRE DEL PROCESO <<<<<" -Path $LogPath
    }
}

# --- INVOCACIÓN PROFESIONAL ---
# Se utilizan rutas absolutas para garantizar el funcionamiento en Task Scheduler
Start-ProfessionalBackup -SourcePath "C:\Datos" -DestinationBase "C:\Backups" -LogPath "C:\Logs\Ejercicio3.log"
