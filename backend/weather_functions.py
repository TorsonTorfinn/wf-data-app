import requests
import streamlit as st

API_KEY = st.secrets["API_KEY"]

def get_data(place, days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url=url)
    data = response.json()

    filtered_data = data['list']
    values_amount = 8 * days 
    filtered_data = filtered_data[:values_amount] # filtered_data[8] -> 1 day 

    return filtered_data

