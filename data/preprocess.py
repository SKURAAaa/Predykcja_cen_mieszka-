"""
Moduł do wczytywania i przetwarzania danych z pliku CSV.
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


def load_and_preprocess_data(file_path: str) -> tuple:
    """
    Wczytuje zbiór danych, usuwa braki i koduje zmienne.

    Args:
        file_path (str): Ścieżka do pliku CSV.

    Returns:
        tuple: Zwraca x_train, x_test, y_train, y_test oraz preprocesor.
    """
    data = pd.read_csv(file_path)
    data = data.dropna()

    x_data = data.drop("median_house_value", axis=1)
    y_data = data["median_house_value"]

    categorical_features = ["ocean_proximity"]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features,
            )
        ],
        remainder="passthrough",
    )

    x_processed = preprocessor.fit_transform(x_data)

    x_train, x_test, y_train, y_test = train_test_split(
        x_processed,
        y_data,
        test_size=0.2,
        random_state=42,
    )

    return x_train, x_test, y_train, y_test, preprocessor