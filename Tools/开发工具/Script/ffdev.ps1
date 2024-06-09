param(
    [string]$program,
    [string]$command,
    [string[]]$inputArgs
)

$parentDir = Split-Path -Path $PSScriptRoot -Parent

if ($program -eq "总调用") {
    $pythonScript = Join-Path $parentDir "总调用.py"
} elseif ($program -eq "目录复制") {
    $pythonScript = Join-Path $parentDir "目录复制.py"
} elseif ($program -eq "参数查重") {
    $pythonScript = Join-Path $parentDir "代码校对\参数查重.py"
} elseif ($program -eq "非UTF-8编码") {
    $pythonScript = Join-Path $parentDir "代码校对\非UTF-8编码.py"
} elseif ($program -eq "尾随空格") {
    $pythonScript = Join-Path $parentDir "代码校对\尾随空格.py"
} elseif ($program -eq "需求生成") {
    $pythonScript = Join-Path $parentDir "生成工具\需求生成.py"
} elseif ($program -eq "代码行数") {
    $pythonScript = Join-Path $parentDir "统计\代码总行数.py"
} elseif ($program -eq "账号切换") {
    $pythonScript = Join-Path $parentDir "git\账号切换.py"
} else {
    Write-Warning "无效的程序调用"
    Write-Output "可用程序: [目录复制] [参数查重] [非UTF-8编码] [尾随空格] [需求生成] [代码行数] [账号切换]"
    $flag = 1
}

if ($flag -ne 1) {
    python $pythonScript $command $inputArgs
}
