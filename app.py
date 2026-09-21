import streamlit as st
import pandas as pd
from datetime import datetime

from data_manager import load_data, save_data, add_observation
from weather_api import get_weather, get_forecast
from ai_meteorologist import get_llm_response

from analysis import (
    average_temperature,
    minimum_temperature,
    maximum_temperature,
    most_common_condition,
    search_by_date,
    temperature_trend,
    filter_by_month,
    filter_by_season,
    predict_tomorrow_weather,
    compare_years,
    temperature_text_graph,
    record_temperatures
    
)

def show_weather_effect(condition, temperature):
    if "rain" in condition.lower():
        st.markdown("<h1 style='text-align: center;'>🌧️🌧️🌧️</h1>", unsafe_allow_html=True)

    elif "snow" in condition.lower():
        st.snow()

    elif temperature >= 40:
        st.markdown("<h1 style='text-align: center;'>🔥🔥🔥</h1>", unsafe_allow_html=True)

    elif "sun" in condition.lower():
        st.markdown("<h1 style='text-align: center;'>☀️☀️☀️</h1>", unsafe_allow_html=True)

    elif "cloud" in condition.lower():
        st.markdown("<h1 style='text-align: center;'>☁️☁️☁️</h1>", unsafe_allow_html=True)

st.title("🌞Weather Tracker🌪️🌡️")

df = load_data()

st.header("🌤️ What would you like to do?")

option = st.selectbox(
    "Choose an option:",
    [
        "📝 Record New Observation",
        "📊 View Weather Statistics",
        "🔎 Search by Date",
        "📋 View All Observations",
        "🗓️ Filter by Month / Season",
        "🌍 Check Live Weather"
    ], index=None,placeholder="Choose an option🖋️ ... "
)

if option == "📝 Record New Observation":
    st.subheader("📝 Record New Weather Observation")

    date = st.text_input("📅 Date (MM-DD-YYYY)")
    temperature = st.number_input("🌡️ Temperature (°C)")
    condition = st.text_input("☁️ Weather Condition")
    humidity = st.number_input("💧 Humidity (%)", min_value=0, max_value=100)
    wind_speed = st.number_input("💨 Wind Speed (km/h)", min_value=0.0)

    if st.button("💾 Save Observation"):
        new_data = pd.DataFrame({
            "date": [date],
            "temperature": [temperature],
            "condition": [condition],
            "humidity": [humidity],
            "wind_speed": [wind_speed]
        })

        df = pd.concat([df, new_data], ignore_index=True)

        save_data(df)

        st.success("✅ Observation saved successfully!")
        show_weather_effect(condition, temperature)

elif option == "📊 View Weather Statistics":
    st.subheader("📊 Weather Statistics")

    average = average_temperature(df)
    minimum = minimum_temperature(df)
    maximum = maximum_temperature(df)
    common_condition = most_common_condition(df)
    trend = temperature_trend(df)
    prediction = predict_tomorrow_weather(df)
    year_comparison = compare_years(df)
    highest_temperature, lowest_temperature = record_temperatures(df)
    temperature_graph = temperature_text_graph(df)


    st.metric("🌡️ Average Temperature", f"{average:.1f} °C")
    st.metric("❄️ Minimum Temperature", f"{minimum} °C")
    st.metric("🔥 Maximum Temperature", f"{maximum} °C")
    st.metric("🏆 Record High Temperature", f"{highest_temperature} °C")
    st.metric("❄️ Record Low Temperature", f"{lowest_temperature} °C")
    st.metric("☁️ Most Common Condition", common_condition)
    st.metric("📈 Temperature Trend", trend)
    st.metric("🔮 Tomorrow's Weather", prediction)
    st.subheader("🌡️ Temperature Trend Graph")
    st.text(temperature_graph)
    

    st.subheader("📊 Average Temperature by Year")
    st.dataframe(year_comparison)


elif option == "🔎 Search by Date":
    st.subheader("🔎 Search Weather by Date")

    search_date = st.text_input("📅 Enter Date (MM-DD-YYYY)")

    if st.button("🔍 Search"):
        result = search_by_date(df, search_date)

        if result.empty:
            st.warning("⚠️ No observation found for this date.")
        else:
            st.success("✅ Observation found!")
            st.dataframe(result)

elif option == "📋 View All Observations":
    st.subheader("📋 All Weather Observations")

    if df.empty:
        st.info("ℹ️ No weather observations recorded yet.")
    else:
        st.dataframe(df)

elif option == "🗓️ Filter by Month / Season":
    st.subheader("🗓️ Filter Weather Data")

    filter_type = st.radio(
        "Choose filter type:",
        ["Month", "Season"]
    )

    if filter_type == "Month":
        month = st.selectbox(
            "Choose a month:",
            range(1, 13)
        )

        if st.button("🔍 Filter by Month"):
            result = filter_by_month(df, month)
            st.dataframe(result)

    else:
        season = st.selectbox(
            "Choose a season:",
            ["Winter", "Spring", "Summer", "Autumn"]
        )

        if st.button("🔍 Filter by Season"):
            result = filter_by_season(df, season)
            st.dataframe(result)

elif option == "🌍 Check Live Weather":
    st.subheader("🌍 Live Weather")

    city = st.text_input("🏙️ Enter a city")

    if st.button("🌤️ Get Weather"):
        weather = get_weather(city)

        if weather is None:
            st.error("❌ City not found.")
        else:
            observation = {
                "date": datetime.now().strftime("%m-%d-%Y"),
                "temperature": weather["temperature"],
                "condition": weather["condition"],
                "humidity": weather["humidity"],
                "wind_speed": weather["wind_speed"]
            }

            add_observation(observation)

            st.success(f"Weather in {weather['city']}")

            st.metric("🌡️ Temperature", f"{weather['temperature']} °C")
            st.metric("💧 Humidity", f"{weather['humidity']} %")
            st.metric("💨 Wind Speed", f"{weather['wind_speed']} km/h")
            st.write(f"☁️ Condition: {weather['condition']}")

            st.subheader("🤖 AI Meteorologist")

            ai_response = get_llm_response(df)

            st.write(ai_response)

            st.subheader("📅 Weather Forecast")

            forecast = get_forecast(city)

            if forecast is None:
                st.error("❌ Could not get the weather forecast.")

            else:
                forecast_rows = []

                for item in forecast["list"]:
                    forecast_rows.append({
                        "Date": item["dt_txt"][:10],
                        "Temperature (°C)": round(item["main"]["temp"] - 273.15, 1),
                        "Condition": item["weather"][0]["description"]
                    })

                forecast_df = pd.DataFrame(forecast_rows)

                forecast_df["Date"] = pd.to_datetime(forecast_df["Date"])

                daily_forecast = forecast_df.groupby("Date").agg(
                    Min_Temperature=("Temperature (°C)", "min"),
                    Max_Temperature=("Temperature (°C)", "max"),
                    Condition=("Condition", "first")
                ).reset_index()

                daily_forecast = daily_forecast.iloc[1:6]

                daily_forecast["Date"] = daily_forecast["Date"].dt.strftime("%m-%d-%Y")

                daily_forecast = daily_forecast.rename(columns={
                    "Date": "Date",
                    "Min_Temperature": "Min Temperature (°C)",
                    "Max_Temperature": "Max Temperature (°C)",
                    "Condition": "Condition"
                })

                st.dataframe(daily_forecast, use_container_width=True)