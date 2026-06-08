@echo off
title California Housing Price Prediction

echo ==========================================
echo California Housing Price Prediction
echo ==========================================
echo.

if not exist ".venv" (
    echo Tworzenie srodowiska Python...
    python -m venv .venv
)

call .venv\Scripts\activate

echo Instalowanie wymaganych pakietow...
pip install -r requirements.txt

echo.
echo Uruchamianie aplikacji...
echo.

streamlit run app\app.py

pause