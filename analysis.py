import pandas as pd

def average_temperature(df):
    """Return the average (AVG) temperature"""
    return df["temperature"].mean()

def minimum_temperature(df):
    """Return the lowest temperature"""
    return df["temperature"].min()

def maximum_temperature(df):
    """Return the highest temperature"""
    return df["temperature"].max()

def most_common_condition(df):
    """Return the most common weather condition"""
    return df["condition"].mode()[0]

def temperature_trend(df):
    """Return whether temperature is increasing or decreasing"""
    df = df.copy() 
    if df.empty:
        return "No data"

    df["date"] = pd.to_datetime(df["date"], format="%m-%d-%Y") # convert the date from str to real date
    df = df.sort_values("date")

    first_temperature = df["temperature"].iloc[0]
    last_temperature = df["temperature"].iloc[-1]

    if last_temperature > first_temperature:
        return "Increasing"

    if last_temperature < first_temperature:
        return "Decreasing"

    return "No change"

def temperature_text_graph(df):
    """Return a text-based temperature graph"""

    df = df.copy()

    if df.empty:
        return "No data"

    df["date"] = pd.to_datetime(df["date"], format="%m-%d-%Y")
    df = df.sort_values("date")

    lines = []

    for _, row in df.iterrows():
        date = row["date"].strftime("%m-%d-%Y")
        temperature = row["temperature"]
        bars = "█" * int(temperature)

        lines.append(
            f"{date} | {bars} {temperature}°C"
        )

    return "\n".join(lines)

def filter_by_month(df, month):
    """Return weather observations for a specific month"""
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], format="%m-%d-%Y")
    return df[df["date"].dt.month == month]

def filter_by_season(df, season):
    """Return weather observations for a specific season"""
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], format="%m-%d-%Y")

    # Dictionary mapping each season to its months
    seasons = {
        "Winter": [12, 1, 2],
        "Spring": [3, 4, 5],
        "Summer": [6, 7, 8],
        "Autumn": [9, 10, 11]
    }

    return df[df["date"].dt.month.isin(seasons[season])]

def predict_tomorrow_weather(df):
    """Predict tomorrow's weather condition based on historical patterns"""
    df = df.copy()
    if df.empty:
        return "No data"

    df["date"] = pd.to_datetime(df["date"], format="%m-%d-%Y")

    latest_date = df["date"].max()
    tomorrow = latest_date + pd.Timedelta(days=1)
    tomorrow_month = tomorrow.month

    historical_data = df[df["date"].dt.month == tomorrow_month]

    if historical_data.empty:
        return "Not enough historical data"

    prediction = historical_data["condition"].mode()[0]

    return prediction

def compare_years(df):
    """Compare average temperatures between years"""
    df = df.copy()
    if df.empty:
        return "No data"

    df["date"] = pd.to_datetime(df["date"], format="%m-%d-%Y")
    df["year"] = df["date"].dt.year

    return df.groupby("year")["temperature"].mean()

def record_temperatures(df):
    """Return the highest and lowest recorded temperatures"""
    if df.empty:
        return "No data"

    highest = df["temperature"].max()
    lowest = df["temperature"].min()

    return highest, lowest

def search_by_date(df, date):
    """Return weather observation for a specific date"""
    return df[df["date"] == date]