import requests
import streamlit as st
import json

st.title("Weather Application")

with open('data.json','r') as file:
    data = json.load(file)

st.write(data)

states = data.keys()
city_name = ""

st.subheader("Select the State")
state_name = st.selectbox(label="Select the State",options=states)

if state_name:
    cities = data[state_name]
    st.subheader("Select the City")
    city_name = st.selectbox(label="Select the City",options=cities)

if city_name:
    api_key = "01935a87d8ebcb7f5154b662dea73747"
url =  f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_name}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
 data = response.json()
 st.write(json.dumps(data, indent=4))
 st.write(f"Current Weather Condition: {data['weather'][0]['main']}")
 st.write(f"Current Temperature: {data['main']['temp']}°C.")
 st.write(f"Temperature Feels Like: {data['main']['feels_like']}°C.")
 st.write(f"Humidity: {data['main']['humidity']}%.")

else:
  st.error("Error Occured, Please check the city name or the state name is correct or not!")    