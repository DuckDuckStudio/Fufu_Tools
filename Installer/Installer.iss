[Setup]
AppName=芙芙工具箱
AppVersion=develop
VersionInfoVersion=develop
AppPublisher=DuckStudio
VersionInfoCopyright=Copyright (c) 鸭鸭「カモ」
AppPublisherURL=https://duckduckstudio.github.io/yazicbs.github.io/
AppSupportURL=https://github.com/DuckDuckStudio/Fufu_Tools/issues
DefaultDirName={autopf}\Fufu_Tools
DefaultGroupName=芙芙工具箱
OutputDir=..\Release
OutputBaseFilename=Fufu_Tools_Setup.vdevelop
SetupIconFile=Fufu_Tools_Setup_ico.ico
LicenseFile=LICENSE
Compression=lzma2
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64compatible

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "chinesesimplified"; MessagesFile: "compiler:Languages\ChineseSimplified.isl"
Name: "japanese"; MessagesFile: "compiler:Languages\Japanese.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "..\Release\Fufu_Tools.vdevelop-exe\*"; DestDir: "{app}"; Flags: recursesubdirs
; 这里的 v 不要去掉，替换版本号时不会替换 v

[Icons]
Name: "{autoprograms}\芙芙工具箱"; Filename: "{app}\芙芙工具箱.exe"
Name: "{autodesktop}\芙芙工具箱"; Filename: "{app}\芙芙工具箱.exe"; Tasks: desktopicon
