@echo off
title Infosys SE Mock Assessment Platform
echo ========================================================
echo   Infosys Systems Engineer (SE) Mock Test Platform
echo   2027 Batch Pattern - Multi-Test Assessment Engine
echo ========================================================
echo.
echo Starting local server on port 8080...
start "" "http://localhost:8080"
python -m http.server 8080
if %errorlevel% neq 0 (
    echo.
    echo Port 8080 busy or Python unavailable.
    echo Opening index.html directly in browser...
    start "" "index.html"
)
pause
