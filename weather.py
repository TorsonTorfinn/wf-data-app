import streamlit as st
from backend.weather_functions import get_data
import plotly.express as px

st.title('Weather Forecast')

place = st.text_input('Enter name if the City:')
days = st.slider('Forecast Days', min_value=1, max_value=5, help='Select the number of forecasted days')
option = st.selectbox('Select the type of weather to view', ('Temperature', 'Sky Conditions'))

st.subheader(f"{option} for the next {days} days in {place}:")

if place:
    filtered_data = get_data(place, days)

    if option == 'Temperature':
        temp_format = st.radio('Pick One of the Temperature Metric', ['Celcius (°C)', 'Fahrenheit (°F)', 'Kelvin (K)'])

        def convert_temp(temp):
            if temp_format == "Celcius (°C)":
                return round(temp - 273.15) # Kelvin - 273.15 = Celcius 
            if temp_format == "Fahrenheit (°F)":
                return round((temp - 273.15) * 9/5 + 32, 2)
            if temp_format == "Kelvin (K)":
                return round(temp)
            
        temperatures = [convert_temp(temp_data['main']['temp']) for temp_data in filtered_data]
        min_temp = convert_temp(min(data['main']['temp_min'] for data in filtered_data))
        max_temp = convert_temp(max(data['main']['temp_max'] for data in filtered_data))
        current_temp = temperatures[0]

        st.metric(label='Current Temperature',
                  value=f"{current_temp} {temp_format.split(' ')[1]}",
                  delta=f"{(max_temp - min_temp):.2f} {temp_format.split(' ')[0]}")
        
        dates = [date['dt_txt'] for date in filtered_data]

        fig = px.line(
            x=dates,
            y=temperatures,
            labels={"x": "Date", "y": f"Temperature {temp_format.split(' ')[1]}"},
            title="Temperature Over Time"
        )
        
        fig.update_layout(
            xaxis_title="Date",
            yaxis_title=f"Temperature ({temp_format.split(' ')[1]}",
            template="plotly_white"
        )

        st.plotly_chart(fig)