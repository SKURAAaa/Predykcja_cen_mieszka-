"""
Moduł odpowiedzialny za trenowanie modelu Random Forest.
"""

# pylint: disable=wrong-import-position,wrong-import-order

import os
import sys
...

# 1. BEZWZGLĘDNE WYMUSZENIE ŚCIEŻKI GŁÓWNEJ
# Pobieramy ścieżkę do folderu, w którym jest ten plik (model)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Pobieramy ścieżkę do folderu wyżej (Predykcja_cen_mieszkań_Grupa5)
parent_dir = os.path.dirname(current_dir)
# Wrzucamy główny folder na ZEROWE miejsce listy ścieżek Pythona
sys.path.insert(0, parent_dir)

# 2. TERAZ DOPIERO IMPORTUJEMY TWOJE PLIKI
from data.preprocess import load_and_preprocess_data

# 3. RESZTA IMPORTÓW
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

def train_model() -> None:
    """Trenuje model Random Forest i zapisuje artefakty."""

    # Budujemy bezpieczne, absolutne ścieżki do plików
    dataset_path = os.path.join(parent_dir, "data", "housing.csv")
    model_path = os.path.join(current_dir, "housing_model.pkl")
    preprocessor_path = os.path.join(current_dir, "preprocessor.pkl")

    print(f"Szukam danych w: {dataset_path}")

    (
        x_train,
        x_test,
        y_train,
        y_test,
        preprocessor
    ) = load_and_preprocess_data(dataset_path)

    print("Trenowanie modelu...")
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1,
    )
    model.fit(x_train, y_train)

    print("Ocena wydajności modelu...")
    predictions = model.predict(x_test)
    score = r2_score(y_test, predictions)
    print(f"R2 score: {score:.4f}")

    # Zapis modeli do dysku
    joblib.dump(model, model_path)
    joblib.dump(preprocessor, preprocessor_path)
    print("Zakończono sukcesem!")

if __name__ == "__main__":
    train_model()