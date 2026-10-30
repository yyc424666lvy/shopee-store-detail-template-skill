param(
    [string]$Destination = (Join-Path $HOME ".workbuddy\skills\shopee-store-detail-template"),
    [switch]$Force
)
$ErrorActionPreference = "Stop"
if (-not (Test-Path $Destination)) {
    Write-Host "Not installed: $Destination"
    exit 0
}
if (-not $Force) {
    Write-Host "This will permanently delete: $Destination"
    Write-Host "There is no backup and no recycle bin. Re-run with -Force to confirm."
    exit 1
}
Remove-Item -Recurse -Force $Destination
Write-Host "Removed: $Destination"
