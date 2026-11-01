# Instala las skills de este repositorio en Claude Code de este PC.
# Uso (desde la carpeta del repo):  powershell -ExecutionPolicy Bypass -File .\instalar.ps1
# Copia cada carpeta de skill a %USERPROFILE%\.claude\skills. Si una ya existe, la vieja se mueve a
# %USERPROFILE%\.claude\skills-respaldo (fuera de skills, para que Claude no la cargue dos veces).

$destino = Join-Path $env:USERPROFILE ".claude\skills"
$respaldos = Join-Path $env:USERPROFILE ".claude\skills-respaldo"
New-Item -ItemType Directory -Force -Path $destino | Out-Null
$skills = Get-ChildItem -Path $PSScriptRoot -Directory | Where-Object { Test-Path (Join-Path $_.FullName "SKILL.md") }
foreach ($s in $skills) {
    $final = Join-Path $destino $s.Name
    if (Test-Path $final) {
        New-Item -ItemType Directory -Force -Path $respaldos | Out-Null
        $viejo = Join-Path $respaldos $s.Name
        if (Test-Path $viejo) { Remove-Item -Recurse -Force $viejo }
        Move-Item -Path $final -Destination $viejo
    }
    Copy-Item -Recurse -Path $s.FullName -Destination $final
    Write-Host "Instalada: $($s.Name)"
}
Write-Host ""
Write-Host "Listo: $($skills.Count) skills en $destino. Cierra y vuelve a abrir Claude Code para que las cargue."
