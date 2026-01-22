<#
.SYNOPSIS
    Monitorización profesional de almacenamiento con trazabilidad y gestión de errores.
    Sigue el principio de mínimos privilegios y diseño modular.
#>

# --- FUNCIÓN DE LOG (Centralizada y Segura) ---
function Write-LogEntry {
    param (
        [Parameter(Mandatory = $true)] [string]$Message,
        [Parameter(Mandatory = $true)] [string]$Path
    )
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

# --- FUNCIÓN DE AUDITORÍA ---
function Start-DiskMonitor {
    param (
        [string]$DriveID = "C:",
        [int]$Limit = 80,
        [string]$LogPath = "C:\GestionMantenimiento\Logs\DiskMonitor.log"
    )

    Write-LogEntry -Message "INICIO: Auditoría de volumen $DriveID" -Path $LogPath

    try {
        # Obtención de datos con control de errores explícito
        $Disk = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='$DriveID'" -ErrorAction Stop
        
        if ($null -eq $Disk) { throw "No se encontró el dispositivo $DriveID" }

        # Cálculos de capacidad
        $Total = $Disk.Size
        $Free = $Disk.FreeSpace
        $UsedPercent = [Math]::Round((($Total - $Free) / $Total) * 100, 2)
        $UsedGB = [Math]::Round(($Total - $Free) / 1GB, 2)

        # Evaluación de umbral
        if ($UsedPercent -gt $Limit) {
            $StatusMsg = "ALERTA: Espacio insuficiente en $DriveID. Uso: $UsedPercent% ($UsedGB GB)."
        } else {
            $StatusMsg = "OK: Uso del volumen $DriveID dentro de límites ($UsedPercent%)."
        }

        Write-LogEntry -Message $StatusMsg -Path $LogPath
    }
    catch {
        # El diagnóstico profesional requiere el detalle del error
        Write-LogEntry -Message "ERROR: $($_.Exception.Message)" -Path $LogPath
        exit 1
    }
    finally {
        Write-LogEntry -Message "FIN: Auditoría finalizada." -Path $LogPath
    }
}

# --- EJECUCIÓN ---
# Se usan parámetros para que el script sea reutilizable y automatizable de verdad
Start-DiskMonitor -DriveID "C:" -Limit 80 -LogPath "C:\GestionMantenimiento\Logs\Ejercicio2.log"
