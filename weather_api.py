import requests


def get_weather(city):
    """Return the current weather for a city"""

    # Find the city's coordinates
    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

    geocoding_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    location_response = requests.get(
        geocoding_url,
        params=geocoding_params
    )

    if location_response.status_code != 200:
        return None

    location_data = location_response.json()

    if "results" not in location_data:
        return None

    latitude = location_data["results"][0]["latitude"]
    longitude = location_data["results"][0]["longitude"]

    # Get current weather
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh",
        "timezone": "auto"
    }

    response = requests.get(
        weather_url,
        params=weather_params
    )

    if response.status_code != 200:
        return None

    data = response.json()

    current = data["current"]

    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm"
    }

    condition = weather_codes.get(
        current["weather_code"],
        "Unknown"
    )

    return {
        "city": city,
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "condition": condition,
        "latitude": latitude,
        "longitude": longitude
    }


def get_forecast(city):
    """Return the weather forecast for the next few days"""

    weather = get_weather(city)

    if weather is None:
        return None

    latitude = weather["latitude"]
    longitude = weather["longitude"]

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_min,temperature_2m_max,weather_code",
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh",
        "timezone": "auto",
        "forecast_days": 6
    }

    response = requests.get(
        url,
        params=params
    )

    if response.status_code != 200:
        return None

    data = response.json()

    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm"
    }

    return {
        "list": [
            {
                "dt_txt": date,
                "main": {
                    "temp": max_temp
                },
                "weather": [
                    {
                        "description": weather_codes.get(
                            code,
                            "Unknown"
                        )
                    }
                ],
                "min_temp": min_temp
            }
            for date, min_temp, max_temp, code in zip(
                data["daily"]["time"],
                data["daily"]["temperature_2m_min"],
                data["daily"]["temperature_2m_max"],
                data["daily"]["weather_code"]
            )
        ]
    }