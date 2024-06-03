param(
    [string]$program,
    [string[]]$inputArgs
)

if ($program -eq "总调用") {
    python D:\Duckhome\projects\MSVS\Source\Repos\Fufu-Tools\Tools\开发工具\总调用.py $inputArgs
} elseif ($program -eq "目录复制") {
    python D:\Duckhome\projects\MSVS\Source\Repos\Fufu-Tools\Tools\开发工具\目录复制.pyw $inputArgs
} elseif ($program -eq "参数查重") {
    python D:\Duckhome\projects\MSVS\Source\Repos\Fufu-Tools\Tools\开发工具\代码校对\参数查重.py $inputArgs
} elseif ($program -eq "非UTF-8编码") {
    python D:\Duckhome\projects\MSVS\Source\Repos\Fufu-Tools\Tools\开发工具\代码校对\非UTF-8编码.py $inputArgs
} elseif ($program -eq "尾随空格") {
    python D:\Duckhome\projects\MSVS\Source\Repos\Fufu-Tools\Tools\开发工具\代码校对\尾随空格.py $inputArgs
} elseif ($program -eq "需求生成") {
    python D:\Duckhome\projects\MSVS\Source\Repos\Fufu-Tools\Tools\开发工具\生成工具\需求生成.py $inputArgs
} elseif ($program -eq "代码行数") {
    python D:\Duckhome\projects\MSVS\Source\Repos\Fufu-Tools\Tools\开发工具\统计\代码总行数.py $inputArgs
} else {
    Write-Warning "无效的程序调用"
    Write-Output "可用程序: [目录复制] [参数查重] [非UTF-8编码] [尾随空格] [需求生成] [代码行数]"
}