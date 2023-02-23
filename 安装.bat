
%1 %2
ver|find "5.">nul&&goto :Admin
mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :Admin","","runas",1)(window.close)&goto :eof
:Admin
set d=%~dp0
set f=%d:~0,2%
%f%
cd %d%
Start  /wait .\Scripts\python.exe .\src\createLogin.py
copy  .\login.bat "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
del .\login.bat
call  "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\login.bat"