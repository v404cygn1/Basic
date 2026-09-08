@echo off
title Gestor de Gastos Personales
cd /d "%~dp0"

:: 1. Verificar si Python esta instalado en la maquina
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no esta instalado o no fue agregado al PATH del sistema.
    echo Por favor instala Python marcando la casilla "Add Python to PATH".
    pause
    exit /b
)

:: 2. Verificar o crear el entorno virtual (.venv)
if not exist ".venv" (
    echo Configurando entorno virtual por primera vez...
    python -m venv .venv
    echo Instalando librerias necesarias...
    call .venv\Scripts\activate
    pip install --upgrade pip
    pip install -r requirements.txt
) else (
    call .venv\Scripts\activate
)

:: 3. Ejecutar el aplicativo
echo Iniciando aplicacion...
python main.py

:: 4. Pausar antes de cerrar para leer posibles errores
pause