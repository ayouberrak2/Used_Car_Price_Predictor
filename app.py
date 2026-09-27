import streamlit as st
import pandas as pd
import joblib


# Charger le modèle
model = joblib.load(
    "models/xgboost_optimise.pkl"
)


st.title("Used Car Price Predictor")

st.write(
    "Entrez les caractéristiques du véhicule "
    "pour obtenir une estimation du prix."
)



year = st.number_input(
    "Année du véhicule",
    min_value=1980,
    max_value=2020,
    value=2018
)


km_driven = st.number_input(
    "Kilométrage",
    min_value=0,
    value=50000
)


brand = st.selectbox(
    "Marque",
    [
        "Maruti",
        "Hyundai",
        "Ford",
        "Toyota",
        "Honda",
        "Mahindra",
        "Tata",
        "Volkswagen",
        "Renault",
        "Nissan",
        "Other"
    ]
)


car_model = st.text_input(
    "Modèle de voiture",
    value="Swift"
)


fuel = st.selectbox(
    "Carburant",
    ["Petrol", "Diesel", "CNG", "LPG", "Electric"]
)


seller_type = st.selectbox(
    "Type de vendeur",
    ["Individual", "Dealer", "Trustmark Dealer"]
)


transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)


owner = st.selectbox(
    "Propriétaire",
    [
        "First Owner",
        "Second Owner",
        "Third Owner",
        "Fourth & Above Owner",
        "Test Drive Car"
    ]
)


# =========================
# Catégorie d'âge
# =========================

age = 2026 - year

if age <= 3:
    age_category = "New"
elif age <= 7:
    age_category = "Mid"
else:
    age_category = "Old"


st.write(f"Catégorie d'âge : **{age_category}**")


# =========================
# Prédiction
# =========================

if st.button("Estimer le prix"):

    vehicle = pd.DataFrame([{
        "year": year,
        "km_driven": km_driven,
        "fuel": fuel,
        "seller_type": seller_type,
        "transmission": transmission,
        "owner": owner,
        "brand": brand,
        "car_model": car_model,
        "age_category": age_category
    }])

    prediction = model.predict(vehicle)

    price = prediction[0]

    st.success(
        f"💰 Prix estimé : {price:,.0f}"
    )