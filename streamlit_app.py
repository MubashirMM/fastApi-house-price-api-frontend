import streamlit as st
import requests

st.set_page_config(page_title="🏠 House Price Predictor", layout="centered")

st.title("🏡 California House Price Predictor")
st.markdown("Enter the details below to get a predicted price:")

# Input fields
MedInc = st.number_input("Median Income", value=4.5)
HouseAge = st.number_input("House Age", value=20.0)
AveRooms = st.number_input("Average Rooms", value=6.0)
AveBedrms = st.number_input("Average Bedrooms", value=1.0)
Population = st.number_input("Population", value=1000.0)
AveOccup = st.number_input("Average Occupancy", value=3.0)
Latitude = st.number_input("Latitude", value=34.0)
Longitude = st.number_input("Longitude", value=-118.0)

if st.button("Predict"):
    # API call to your FastAPI backend
    api_url = "https://mhammadmubashir-fastapi-xgboost-house-price.hf.space/predict"
    payload = {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude
    }

    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            result = response.json()
            st.write("🔍 API raw response:", result)

            st.success(f"💰 Predicted House Price: {result['predicted_price']:.2f}")

        else:
            st.error(f"API Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"API call fail: {e}")
