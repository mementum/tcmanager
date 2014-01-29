; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

; NOTE: the base directory is the one where the script resides and not
; the directory the tool is calling it from
; hence the ..\build\xxxx to fall down to the base directory

#define MyAppName "tcmanager"
#define MyAppVersion "0.0.6"
#define MyAppPublisher "Daniel Rodriguez"
#define MyAppYear "2014"
#define MyAppURL "https://github.com/mementum/tcmanager"
#define MyAppExeName "tcmanager.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
; The fist { is needed as an escape character
AppID={{BDC740C1-731C-4FF2-8255-F4E4745F19C4}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
LicenseFile=..\build\innosetup\LICENSE
;InfoBeforeFile=..\build\innosetup\README.md
OutputBaseFilename={#MyAppName}-{#MyAppVersion}-setup
Compression=lzma2/Ultra64
SolidCompression=false
OutputDir=..\dist\innosetup
AppVerName={#MyAppVersion}
InternalCompressLevel=Ultra64
ShowLanguageDialog=no
AppCopyright=Copyright (C) {#MyAppYear} {#MyAppPublisher}
; SetupIconFile=..\build\innosetup\icons\{#MyAppName}.ico
; For updates
UsePreviousAppDir=yes
CreateUninstallRegKey=no
UpdateUninstallLogAppName=false

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; 
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1

[Files]
Source: ..\build\innosetup\*; DestDir: {app}; Flags: ignoreversion recursesubdirs createallsubdirs uninsremovereadonly; 
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:ProgramOnTheWeb,{#MyAppName}}"; Filename: "{#MyAppURL}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, "&", "&&")}}"; Flags: nowait postinstall skipifsilent

[CustomMessages]

[InnoIDE_Settings]
UseRelativePaths=true

[Registry]
root: HKCU; subkey: Software\{#MyAppName}; valuedata: ""; Flags: UninsDeleteKey; valuetype: none; 
root: HKCU; subkey: Software\{#MyAppName}\{#MyAppName}; valuedata: ""; Flags: UninsDeleteKey; valuetype: none; 
