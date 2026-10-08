@echo off
title BEP Script Yerel Sunucu
echo ===================================================
echo   BEP Script Yerel Sunucu Baslatiliyor...
echo   Standart Surum:     http://localhost:8000
echo   Temel (Saha) Surum: http://localhost:8000/index2.html
echo   Durdurmak icin: Pencereyi kapatin veya Ctrl+C basin.
echo ===================================================
echo.
start http://localhost:8000
python -m http.server 8000
pause
