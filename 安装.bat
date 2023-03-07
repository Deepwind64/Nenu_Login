@chcp 65001
@%1 %2
@ver|find "5.">nul&&goto :Admin
@mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :Admin","","runas",1)(window.close)&goto :eof
@:Admin
@set d=%~dp0
@set f=%d:~0,2%
@set py="C:\Program Files\Python311\python.exe"

@%f%
@cd %d%

@if not exist %py% (set /p flag=该计算机未在指定位置安装 Python3.11 ，是否现在安装？ y/n ) else (goto setup)
@if %flag%==y start /wait .\python-3.11.2-amd64.exe
@if %flag%==n goto leave

:setup
@Start  /wait .\Scripts\python.exe .\src\createLogin.py
@copy  .\login.bat "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
@del .\login.bat
@call  "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\login.bat"
@echo.
@echo 安装成功
@echo.
@pause

:leave
@echo.
@echo 安装失败
@echo.
@pause
exit