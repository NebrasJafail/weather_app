#import os
#import requests
#from dotenv import load_dotenv

#load_dotenv()

import streamlit as st
import requests

def get_weather(city):
    url = "https://open-weather13.p.rapidapi.com/city"

    querystring = {
        "city": city,
        "lang": "EN",
        "units": "metric"
    }

    headers = {
        #"x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
        "x-rapidapi-key": st.secrets["RAPIDAPI_KEY"],
        "x-rapidapi-host": "open-weather13.p.rapidapi.com"
    }

    response = requests.get(
        url,
        headers=headers,
        params=querystring
    )

    if response.status_code != 200:
        return None

    data = response.json()

    print("TYPE:", type(data))
    print("DATA:", data)

    if not isinstance(data, dict):
        return None

    if "main" not in data:
        return None



    temperature = (data["main"]["temp"] - 32) * 5 / 9
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"] * 3.6
    condition = data["weather"][0]["description"]

    return {
    "city": city,
    "temperature": round(temperature, 2),
    "humidity": humidity,
    "wind_speed": wind_speed,
    "condition": condition,
    "latitude": data["coord"]["lat"],
    "longitude": data["coord"]["lon"]
}

def get_forecast(city):
    """Return the weather forecast for the next few days"""

    current_weather = get_weather(city)

    if current_weather is None:
        return None

    latitude = current_weather["latitude"]
    longitude = current_weather["longitude"]

    url = "https://open-weather13.p.rapidapi.com/fivedaysforcast"

    querystring = {
        "lang": "EN",
        "longitude": str(longitude),
        "latitude": str(latitude)
    }

    headers = {
        #"x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
        "x-rapidapi-key": st.secrets["RAPIDAPI_KEY"],        
        "x-rapidapi-host": "open-weather13.p.rapidapi.com"
    }

    response = requests.get(
        url,
        headers=headers,
        params=querystring
    )

    if response.status_code != 200:
        return None

    return response.json()

    