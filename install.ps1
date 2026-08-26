param([string]$Destination = (Join-Path $HOME ".workbuddy\skills\shopee-store-detail-template"))
$ErrorActionPreference = "Stop"
$Source = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not (Test-Path (Join-Path $Source "SKILL.md"))) { throw "SKILL.md not found in repository root." }
$Parent = Split-Path -Parent $Destination
New-Item -ItemType Directory -Force -Path $Parent | Out-Null
if (Test-Path $Destination) { Remove-Item -Recurse -Force $Destination }
New-Item -ItemType Directory -Force -Path $Destination | Out-Null
$Exclude = @('.git', '__pycache__')
Get-ChildItem -Force $Source | Where-Object { $Exclude -notcontains $_.Name } | ForEach-Object { Copy-Item -Recurse -Force $_.FullName -Destination $Destination }
Write-Host "Installed: $Destination"
Write-Host "Restart WorkBuddy or reload skills, then use /skills to verify."
