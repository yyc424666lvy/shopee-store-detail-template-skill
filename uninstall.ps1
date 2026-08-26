param([string]$Destination = (Join-Path $HOME ".workbuddy\skills\shopee-store-detail-template"))
$ErrorActionPreference = "Stop"
if (Test-Path $Destination) { Remove-Item -Recurse -Force $Destination; Write-Host "Removed: $Destination" } else { Write-Host "Not installed: $Destination" }
