param(
    [ValidateSet('idle', 'move', 'palette', 'form', 'transform')][string]$Kind = 'idle',
    [int]$PlayerSpecies = 277,
    [int]$EnemySpecies = 286,
    [int]$Move = 1,
    [uint32]$Personality = 0,
    [ValidateRange(0, 2)][int]$Side = 2,
    [ValidateRange(0, 1)][int]$Shiny = 0,
    [Parameter(Mandatory = $true)][string]$Name,
    [ValidateRange(0, 2)][int]$DeoxysPreview = 0,
    [switch]$ReturnNormal,
    [switch]$Overwrite
)

# Only manage our isolated test executable and SD. Never stop the user's
# Azahar instance or write its ordinary SD/save/configuration directory.
$taskRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$taskExe = Join-Path $taskRoot 'build/bw2-azahar/bw2-test.exe'
$taskBinary = Join-Path $taskRoot 'build/bw2-validation/validation.3dsx'
$taskPidFile = Join-Path $taskRoot 'build/bw2-validation/emulator.pid'
$taskOutputRoot = [IO.Path]::GetFullPath((Join-Path $taskRoot 'build/bw2-validation'))
$taskOutput = [IO.Path]::GetFullPath((Join-Path $taskOutputRoot $Name))
if (-not $taskOutput.StartsWith($taskOutputRoot + [IO.Path]::DirectorySeparatorChar)) {
    throw 'Capture output must remain inside the isolated validation directory.'
}
if (-not (Test-Path -LiteralPath $taskExe) -or -not (Test-Path -LiteralPath $taskBinary)) {
    throw 'Build the validation executable and prepare the isolated emulator first.'
}
$taskPreviousReport = Join-Path $taskOutput 'capture.json'
if ((Test-Path -LiteralPath $taskPreviousReport) -and -not $Overwrite) {
    $taskPrevious = Get-Content -Raw -LiteralPath $taskPreviousReport | ConvertFrom-Json
    $taskHash = (Get-FileHash -LiteralPath $taskBinary).Hash.ToLowerInvariant()
    if ($taskPrevious.passed -and $taskPrevious.binary_sha256 -eq $taskHash -and
        $taskPrevious.scenario.player -eq $PlayerSpecies -and $taskPrevious.scenario.enemy -eq $EnemySpecies -and
        $taskPrevious.scenario.move -eq $Move -and $taskPrevious.scenario.side -eq $Side -and
        $taskPrevious.scenario.shiny -eq $Shiny -and [int]$taskPrevious.scenario.deoxys_preview -eq $DeoxysPreview -and [bool]$taskPrevious.scenario.return_normal -eq [bool]$ReturnNormal -and [uint32]$taskPrevious.scenario.personality -eq $Personality -and $taskPrevious.kind -eq $Kind) {
        Write-Output "Verified capture already exists: $Name"
        exit 0
    }
    throw 'Capture exists with another scenario/build. Use a new name or explicitly overwrite it.'
}
if (Test-Path -LiteralPath $taskPidFile) {
    $taskOldPid = [int](Get-Content -LiteralPath $taskPidFile)
    $taskOld = Get-CimInstance Win32_Process -Filter "ProcessId=$taskOldPid"
    if ($taskOld -and $taskOld.ExecutablePath -eq $taskExe) {
        Stop-Process -Id $taskOldPid
    }
}
$taskConfig = Join-Path $taskRoot 'build/bw2-azahar/user/sdmc/3ds/emerald3ds/bw2-validation.txt'
$taskSettings = "player=$PlayerSpecies`nenemy=$EnemySpecies`nmove=$Move`nshiny=$Shiny`nseed=4660`nside=$Side`npersonality=$Personality`ndeoxys_preview=$DeoxysPreview`n"
[IO.File]::WriteAllText($taskConfig, $taskSettings)
# Native frame capture requires a rendering window. The user requested these
# demonstrations; minimising this test window can suspend screenshot delivery.
$taskProcess = Start-Process -FilePath $taskExe -ArgumentList ('"' + $taskBinary + '"') -WindowStyle Normal -PassThru
$taskProcess.Id | Set-Content -LiteralPath $taskPidFile
$taskPython = 'C:\Users\rzero\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$taskScript='bw2_capture.py'
if ($Kind -eq 'form') {$taskScript='bw2_capture_forms.py'}
$taskArgs = @('-B', (Join-Path $PSScriptRoot $taskScript), '--kind', $Kind, '--output', $taskOutput)
if ($ReturnNormal) {$taskArgs += '--return-normal'}
if ($Overwrite) { $taskArgs += '--overwrite' }
& $taskPython @taskArgs
$taskStatus = $LASTEXITCODE
$taskLog = Join-Path $taskRoot 'build/bw2-azahar/user/sdmc/3ds/emerald3ds/port.log'
if (Test-Path -LiteralPath $taskOutput) {
    Copy-Item -LiteralPath $taskLog -Destination (Join-Path $taskOutput 'emulator.log')
}
exit $taskStatus
