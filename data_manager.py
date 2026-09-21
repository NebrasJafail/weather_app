import pandas as pd

def load_data():
    return pd.read_csv("weather_data.csv")

def save_data(df):
    df.to_csv("weather_data.csv", index=False)  # no index column

def add_observation(observation):
    """Add a new weather observation to the CSV file"""
    df = load_data()

    new_row = pd.DataFrame([observation])

    df = pd.concat([df, new_row], ignore_index=True)

    save_data(df)