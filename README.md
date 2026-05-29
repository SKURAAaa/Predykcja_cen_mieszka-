# California Housing Price Prediction

## Opis projektu

Celem projektu jest stworzenie aplikacji wykorzystującej model uczenia maszynowego do przewidywania mediany wartości nieruchomości w Kalifornii na podstawie danych geograficznych i demograficznych.

Projekt wykorzystuje algorytm **Random Forest Regressor**, który został wytrenowany na zbiorze danych California Housing Dataset.

Aplikacja umożliwia użytkownikowi wprowadzenie parametrów nieruchomości za pomocą interfejsu webowego stworzonego w technologii Streamlit oraz uzyskanie przewidywanej wartości nieruchomości.

---

## Architektura projektu

Projekt został zbudowany zgodnie z zasadą rozdzielenia odpowiedzialności:

### data/

Moduł odpowiedzialny za:

* wczytywanie danych,
* usuwanie brakujących wartości,
* przygotowanie danych do trenowania,
* kodowanie zmiennych kategorycznych.

### model/

Moduł odpowiedzialny za:

* trenowanie modelu Random Forest,
* ocenę jakości modelu,
* zapis modelu oraz preprocesora do plików `.pkl`,
* generowanie predykcji.

### app/

Moduł odpowiedzialny za:

* uruchomienie aplikacji webowej,
* pobieranie danych od użytkownika,
* wyświetlanie wyników predykcji.

---

## Wykorzystane technologie

* Python 3.x
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib
* Pylint

---

## Wyniki modelu

Model został wytrenowany przy użyciu algorytmu Random Forest Regressor.

Uzyskany wynik:

R² Score = 0.8257

Oznacza to, że model wyjaśnia około 82,57% zmienności cen nieruchomości w zbiorze testowym.

---

## Instalacja projektu

### 1. Klonowanie repozytorium

```bash
git clone <adres_repozytorium>
cd Predykcja_cen_mieszkań_Grupa5
```

### 2. Utworzenie środowiska wirtualnego

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalacja zależności

```bash
pip install -r requirements.txt
```

---

## Trenowanie modelu

Aby wytrenować model:

```bash
python model/train.py
```

Po zakończeniu trenowania zostaną utworzone pliki:

```text
model/housing_model.pkl
model/preprocessor.pkl
```

---

## Uruchomienie aplikacji

```bash
streamlit run app/app.py
```

Po uruchomieniu aplikacja będzie dostępna pod adresem:

```text
http://localhost:8501
```

---

## Dane wejściowe

Użytkownik podaje:

* Longitude
* Latitude
* Housing Median Age
* Total Rooms
* Total Bedrooms
* Population
* Households
* Median Income
* Ocean Proximity

Na podstawie tych danych model przewiduje:

* Median House Value

---

## Struktura projektu

```text
Predykcja_cen_mieszkań_Grupa5
│
├── app/
│   └── app.py
│
├── data/
│   ├── housing.csv
│   ├── preprocess.py
│   └── __init__.py
│
├── model/
│   ├── train.py
│   ├── predict.py
│   ├── housing_model.pkl
│   ├── preprocessor.pkl
│   └── __init__.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---
