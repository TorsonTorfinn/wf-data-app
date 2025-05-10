import streamlit as st

st.title('Weather Forecast')

place = st.text_input('Enter name if the City:')
days = st.slider('Forecast Days', min_value=1, max_value=5, help='Select the number of forecasted days')
option = st.selectbox('Select the type of weather to view', ('Temperature', 'Sky Conditions'))

st.subheader(f"{option} for the next {days} days in {place}:")