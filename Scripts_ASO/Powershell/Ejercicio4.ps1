<#
.SYNOPSIS
    Gestión profesional de logs: Rotación y Purga.
    Evita que los logs crezcan sin control y elimina los obsoletos.
#>

# --- FUNCIÓN DE LOG (Modular y con Timestamp obligatorio) ---
function Write-ProfessionalLog {
    param (
        [Parameter(Mandatory = $true)] [string]$Message,
        [Parameter(Mandatory = $true)] [string]$LogPath
    )
    # Formato de fecha para trazabilidad y diagnóstico profesional
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $Entry = "[$Timestamp] $Message"
    
    try {
        $Dir = Split-Path $LogPath
        if (-not (Test-Path $Dir)) { New-Item -ItemType Directory -Path $Dir -Force | Out-Null }
        Add-Content -Path $LogPath -Value $Entry -Encoding utf8
    }
    catch {
        Write-Error "Fallo crítico escribiendo log: $($_.Exception.Message)"
        exit 1
    }
}

# --- FUNCIÓN DE MANTENIMIENTO ---
function Start-LogMaintenance {
    param (
        [string]$TargetDir = "C:\Logs",
        [int]$DaysToArchive = 7,
        [int]$DaysToDelete = 30,
        [string]$StatusLog = "C:\GestionMantenimiento\Logs\Mantenimiento_Logs.log"
    )

    Write-ProfessionalLog -Message "===== INICIO: Tarea de Rotación y Purga =====" -LogPath $StatusLog

    try {
        if (-not (Test-Path $TargetDir)) { throw "La ruta de logs no existe: $TargetDir" }

        # 1. PURGA: Elimina registros que ya no son útiles (Seguridad de espacio)
        $CutOffDelete = (Get-Date).AddDays(-$DaysToDelete)
        $OldFiles = Get-ChildItem -Path $TargetDir -Recurse | Where-Object { $_.LastWriteTime -lt $CutOffDelete }
        $CountDelete = ($OldFiles | Measure-Object).Count

        if ($CountDelete -gt 0) {
            Write-ProfessionalLog -Message "PURGA: Eliminando $CountDelete archivos obsoletos." -LogPath $StatusLog
            $OldFiles | Remove-Item -Force -ErrorAction Stop
        }

        # 2. ROTACIÓN: Comprime logs antiguos para conservar espacio
        $CutOffArchive = (Get-Date).AddDays(-$DaysToArchive)
        # Filtramos para no re-comprimir lo ya zipeado
        $LogsToRotate = Get-ChildItem -Path $TargetDir -Filter "*.log" | Where-Object { 
            $_.LastWriteTime -lt $CutOffArchive -and $_.FullName -ne $StatusLog 
        }

        foreach ($Log in $LogsToRotate) {
            Write-ProfessionalLog -Message "ROTACIÓN: Comprimiendo $($Log.Name)" -LogPath $StatusLog
            # Se usa -ErrorAction Stop para asegurar que si falla la compresión, no borre el original
            Compress-Archive -Path $Log.FullName -DestinationPath "$($Log.FullName).zip" -Update -ErrorAction Stop
            Remove-Item $Log.FullName -Force -ErrorAction Stop
        }

        Write-ProfessionalLog -Message "STATUS: Mantenimiento finalizado con éxito." -LogPath $StatusLog
    }
    catch {
        Write-ProfessionalLog -Message "ERROR: $($_.Exception.Message)" -LogPath $StatusLog
        exit 1
    }
    finally {
        Write-ProfessionalLog -Message "===== FIN DE TAREA =====" -LogPath $StatusLog
    }
}

# --- EJECUCIÓN (Rutas absolutas para automatización real) ---
Start-LogMaintenance -TargetDir "C:\Logs" -DaysToArchive 7 -DaysToDelete 30 -StatusLog "C:\GestionMantenimiento\Logs\Ejercicio4.log"
