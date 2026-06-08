@echo off
title California Housing Price Prediction

echo ==========================================
echo California Housing Price Prediction
echo ==========================================
echo.

REM Sprawdzenie czy Python jest dostepny
python --version >nul 2>&1
if errorlevel 1 (
    echo Python nie jest zainstalowany lub nie znajduje sie w PATH.
    echo.
    echo Pobierz Python:
    echo https://www.python.org/downloads/
    pause
    exit
)

REM Tworzenie srodowiska jezeli nie istnieje
if not exist ".venv" (
    echo Tworzenie srodowiska Python...
    python -m venv .venv
)

REM Aktywacja srodowiska
call .venv\Scripts\activate

echo Instalowanie wymaganych pakietow...
python -m pip install -r requirements.txt

REM Trenowanie modelu jesli nie istnieje
if not exist "model\model.pkl" (
    echo.
    echo Nie znaleziono modelu.
    echo Rozpoczynam trenowanie...
    python model\train.py
)

echo.
echo Uruchamianie aplikacji...
echo.

python -m streamlit run app\app.py

pause