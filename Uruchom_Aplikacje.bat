@echo off
title California Housing Price Prediction

echo ==========================================
echo California Housing Price Prediction
echo ==========================================
echo.

python --version >nul 2>&1

if errorlevel 1 (
    echo.
    echo Python nie jest zainstalowany lub nie znajduje sie w PATH.
    echo.
    echo Zainstaluj Python ze strony:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit
)

if not exist ".venv" (
    echo Tworzenie srodowiska Python...
    python -m venv .venv
)

call .venv\Scripts\activate

echo Instalowanie wymaganych pakietow...
python -m pip install -r requirements.txt

echo.
echo Uruchamianie aplikacji...
echo.

python -m streamlit run app\app.py

pause