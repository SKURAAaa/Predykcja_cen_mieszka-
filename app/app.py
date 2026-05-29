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
    st.set_page_config(page_title="California Housing")
    st.title("California Housing Price Prediction")

    col1, col2 = st.columns(2)

    with col1:
        longitude = st.number_input("Longitude", value=-122.23)
        latitude = st.number_input("Latitude", value=37.88)
        housing_median_age = st.number_input("Housing Median Age", value=20.0)
        total_rooms = st.number_input("Total Rooms", value=2000.0)

    with col2:
        total_bedrooms = st.number_input("Total Bedrooms", value=400.0)
        population = st.number_input("Population", value=1000.0)
        households = st.number_input("Households", value=350.0)
        median_income = st.number_input("Median Income", value=5.0)

    ocean_proximity = st.selectbox(
        "Ocean Proximity",
        ["<1H OCEAN", "INLAND", "NEAR BAY", "NEAR OCEAN", "ISLAND"],
    )

    if st.button("Predict Price", type="primary"):
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
            st.success(f"Estimated House Value: **${price:,.2f}**")
        except FileNotFoundError as err:
            st.error(str(err))


if __name__ == "__main__":
    main()