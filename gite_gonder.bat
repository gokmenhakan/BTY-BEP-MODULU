@echo off
title GitHub'a Gonder
echo ===================================================
echo   BEP Script - GitHub'a Gonderiliyor...
echo ===================================================
echo.
where git >nul 2>nul
if %ERRORLEVEL% equ 0 (
    git push origin main
) else (
    "%LOCALAPPDATA%\Programs\Git\cmd\git.exe" push origin main
)
echo.
pause
