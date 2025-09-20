
$reg = Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*,HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* | Where-Object DisplayName -match "mixing-station-pc|mixing-station" | Where-Object Publisher -match "dev-core"

$reg | ForEach-Object {
    $path = $_.InstallLocation
    $path = $path.TrimEnd("\\")

    # Safety
    if($path.EndsWith("mixing-station-pc")) {
        Write-Output "Removing old files in $path"
        if(Test-Path $path){
            Remove-Item $path -Recurse
        }
    } else {
        Write-Output "Mixing Station was installed in a non-default location, please manually remove: $path"
    }

    Write-Output "Cleanup registry for $path"
    Remove-Item -Path $_.PSPath

}

$reg = Get-ItemProperty HKCU:\Software\Microsoft\Installer\Products\* | Where-Object ProductName -match "mixing-station-pc|mixing-station"
$reg | ForEach-Object {
    $path = $_.PSPath
    Write-Output "Cleanup installer registry $path"
    Remove-Item -Path $_.PSPath -Recurse
}

$path = "HKCU:\Software\dev-core"
if (Test-Path $path) {
    Remove-Item -Path $path -Recurse
}

Write-Output "Cleanup complete, please re-install Mixing Station"