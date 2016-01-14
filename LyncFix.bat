@echo off

REM @version 1.0.20160113

goto checkIfAdmin

:checkIfAdmin
	net session >nul 2>&1
	
	if NOT %errorLevel% == 0 (
		echo Pleae run as Admin
		pause
		exit
	)

echo Do you with to close Lync and Outlook?
echo Press CTRL + C to cancel or
pause
echo Stopping Lync and Outlook...
timeout 3 >nul
taskkill.exe /F /IM lync.exe
taskkill.exe /F /IM outlook.exe

echo Please wait...
timeout 2 >nul
REG ADD "HKLM\Software\Policies\Microsoft\Office\15.0\Lync" /v "GALDownloadInitialDelay" /t REG_DWORD /d 0 /f
REG ADD "HKLM\Software\Wow6432Node\Policies\Microsoft\Office\15.0\Lync" /v "GALDownloadInitialDelay" /t REG_DWORD /d 0 /f
REG ADD "HKLM\Software\Policies\Microsoft\Communicator" /v "GALDownloadInitialDelay" /t REG_DWORD /d 0 /f
timeout 2 >nul

echo Attempting to start Outlook and Lync...
timeout 3 >nul
if exist "C:\Program Files (x86)\Microsoft Office\Office15\lync.exe" (
	start /D "C:\Program Files (x86)\Microsoft Office\Office15\" lync.exe
) else (
	echo Unable to start Lync!
	echo You will have to start it manually
)

if exist "C:\Program Files (x86)\Microsoft Office\Office15\OUTLOOK.exe" (
	start /D "C:\Program Files (x86)\Microsoft Office\Office15\" OUTLOOK.exe
) else (
	echo Unable to start Outlook!
	echo You will have to start it manually
)

echo Done!
pause
