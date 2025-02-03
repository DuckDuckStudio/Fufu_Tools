param(
    [string]$tool,
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$Args
)

$parentDir = Split-Path -Path $PSScriptRoot -Parent
$version = "develop"
$flag = 0

if ($tool -eq "总调用") {
    $pythonScript = Join-Path $parentDir "总调用.py"
} elseif ($tool -eq "目录复制") {
    $pythonScript = Join-Path $parentDir "目录复制.pyw"
} elseif ($tool -eq "参数查重") {
    $pythonScript = Join-Path $parentDir "代码校对\参数查重.py"
} elseif ($tool -eq "非UTF-8编码") {
    $pythonScript = Join-Path $parentDir "代码校对\非UTF-8编码.py"
} elseif ($tool -eq "尾随空格") {
    $pythonScript = Join-Path $parentDir "代码校对\尾随空格.py"
} elseif ($tool -eq "末尾空行") {
    $pythonScript = Join-Path $parentDir "代码校对\末尾空行.py"
} elseif ($tool -eq "需求生成") {
    $pythonScript = Join-Path $parentDir "生成工具\需求生成.py"
} elseif ($tool -eq "代码行数") {
    $pythonScript = Join-Path $parentDir "统计\代码总行数.py"
} elseif ($tool -eq "账号切换") {
    $pythonScript = Join-Path $parentDir "git\账号切换.py"
} elseif ($tool -eq "连续push") {
    $pythonScript = Join-Path $parentDir "git\连续push尝试.py"
} elseif ($tool -eq "连续pull") {
    $pythonScript = Join-Path $parentDir "git\连续pull尝试.py"
} elseif ($tool -eq "git连续尝试") {
    $pythonScript = Join-Path $parentDir "git\git连续尝试.py"
} elseif ($tool -in "ver", "版本", "version", "Version", "--version", "--ver", "-v") {
    Write-Output "版本: $version"
    Write-Output "安装在: $parentDir"
    $flag = 1
} else {
    Write-Warning "无效的程序调用"
    Write-Output "可用程序: [目录复制] [参数查重] [非UTF-8编码] [尾随空格] [需求生成] [代码行数] [账号切换] [连续push] [连续pull] [git连续尝试]"
    $flag = 1
}

if ($flag -ne 1) {
    python $pythonScript $Args
}
