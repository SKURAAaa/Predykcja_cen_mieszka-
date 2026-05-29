"""
Moduł odpowiedzialny za trenowanie modelu Random Forest.
"""

# pylint: disable=wrong-import-position,wrong-import-order

import os
import sys
...

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from data.preprocess import load_and_preprocess_data

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