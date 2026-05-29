"""
Moduł obsługujący ładowanie modelu i generowanie predykcji.
"""
import sys
from pathlib import Path
import pandas as pd
import joblib

# Dodanie ścieżki głównej
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))


def predict_house_price(input_data: dict) -> float:
    """
    Ładuje zapisany model i przewiduje cenę dla nowych danych.

    Args:
        input_data (dict): Dane wejściowe pobrane z aplikacji Streamlit.

    Returns:
        float: Przewidywana cena nieruchomości.
    """
    model_path = ROOT_DIR / "model" / "housing_model.pkl"
    preprocessor_path = ROOT_DIR / "model" / "preprocessor.pkl"

    if not model_path.exists() or not preprocessor_path.exists():
        raise FileNotFoundError(
            "Brak plików modelu! Uruchom najpierw skrypt model/train.py"
        )

    model = joblib.load(model_path)
    preprocessor = joblib.load(preprocessor_path)

    dataframe = pd.DataFrame([input_data])
    processed = preprocessor.transform(dataframe)
    prediction = model.predict(processed)

    return float(prediction[0])