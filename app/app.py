"""
Moduł interfejsu graficznego (GUI) Streamlit.
"""
import sys
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

# pylint: disable=wrong-import-position
from model.predict import predict_house_price


def main() -> None:
    """Główna funkcja budująca interfejs Streamlit."""
    st.set_page_config(
        page_title="California Housing Prediction",
        page_icon="🏠"
    )

    st.title("🏠 California Housing Price Prediction")

    st.info(
        """
        Wprowadź parametry wybranej okolicy w Kalifornii.
        Aplikacja wykorzystuje model Machine Learning do oszacowania
        wartości nieruchomości na podstawie danych demograficznych
        i geograficznych.
        """
    )

    st.markdown("### Parametry lokalizacji")

    col1, col2 = st.columns(2)

    with col1:
        longitude = st.number_input(
            "Longitude (położenie wschód-zachód)",
            value=-122.23
        )

        latitude = st.number_input(
            "Latitude (położenie północ-południe)",
            value=37.88
        )

        housing_median_age = st.number_input(
            "Średni wiek budynków w okolicy (lata)",
            min_value=1.0,
            value=20.0
        )

        total_rooms = st.number_input(
            "Łączna liczba pokoi w okolicy",
            min_value=1.0,
            value=2000.0,
            help="Typowe wartości: 1000 - 3000"
        )

    with col2:
        total_bedrooms = st.number_input(
            "Łączna liczba sypialni w okolicy",
            min_value=1.0,
            value=400.0,
            help="Typowe wartości: 200 - 700"
        )

        population = st.number_input(
            "Liczba mieszkańców okolicy",
            min_value=1.0,
            value=1000.0,
            help="Typowe wartości: 500 - 2000"
        )

        households = st.number_input(
            "Liczba gospodarstw domowych",
            min_value=1.0,
            value=350.0,
            help="Typowe wartości: 200 - 700"
        )

        median_income = st.number_input(
            "Średni dochód mieszkańców",
            min_value=0.1,
            value=5.0,
            help="Wyższa wartość zwykle oznacza droższe nieruchomości"
        )

    st.markdown("### Odległość od oceanu")

    ocean_proximity = st.selectbox(
        "Położenie względem oceanu",
        ["<1H OCEAN", "INLAND", "NEAR BAY", "NEAR OCEAN", "ISLAND"],
    )

    st.markdown("---")

    st.markdown(
        """
        #### Jak wpływać na wynik?

        📈 Wyższa cena nieruchomości:
        - wyższy średni dochód mieszkańców,
        - atrakcyjniejsza lokalizacja,
        - bliskość oceanu,
        - nowsza zabudowa.

        📉 Niższa cena nieruchomości:
        - niższy dochód mieszkańców,
        - mniej atrakcyjna lokalizacja,
        - starsza zabudowa.
        """
    )

    if st.button("🔍 Oblicz przewidywaną cenę", type="primary"):

        data = {
            "longitude": longitude,
            "latitude": latitude,
            "housing_median_age": housing_median_age,
            "total_rooms": total_rooms,
            "total_bedrooms": total_bedrooms,
            "population": population,
            "households": households,
            "median_income": median_income,
            "ocean_proximity": ocean_proximity,
        }

        try:
            price = predict_house_price(data)

            st.success(
                f"🏠 Przewidywana wartość nieruchomości: "
                f"${price:,.0f}"
            )

        except FileNotFoundError as err:
            st.error(str(err))


if __name__ == "__main__":
    main()