import streamlit as st  
import requests  

st.title("✈️ Flight Price Prediction")  

# Input Fields  
airline = st.number_input("Airline (0-5):", 0, 5)  
source = st.number_input("Source (0-5):", 0, 5)  
destination = st.number_input("Destination (0-5):", 0, 5)  
stops = st.number_input("Number of Stops:", 0, 5)  
duration = st.number_input("Duration (minutes):", 0, 1000)  

if st.button("Predict Price"):  
    data = {  
        "Airline": airline,  
        "Source": source,  
        "Destination": destination,  
        "Stops": stops,  
        "Duration": duration  
    }  
    response = requests.post("http://127.0.0.1:5000/predict", json=data)  
    st.success(f'Predicted Flight Price: ${response.json()["Predicted Price"]:.2f}')  
 
