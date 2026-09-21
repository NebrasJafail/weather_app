#import os #To securely access the API key from the environment variable.
#from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd

#load_dotenv() #Load the variables stored in the .env file.

#client = OpenAI(
 #   base_url="https://openrouter.ai/api/v1",
  #  api_key=os.getenv("OPENROUTER_API_KEY")
#)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"]
)

def get_llm_response(df):
    """Generate an AI weather summary from the latest 7 observations"""

    if df.empty:
        return "No historical weather data available."

    rdf = df.copy()
    df["date"] = pd.to_datetime(df["date"], format="mixed")
    latest_date = df["date"].max()
    recent_data = df[df["date"] >= latest_date - pd.Timedelta(days=6)]

    weather_history = recent_data.to_string(index=False)

    prompt = f"""
    Analyze the following recent weather observations.

    Give a short weather summary in English.
    Mention temperature patterns, common weather conditions,
    and give practical recommendations.

    Recent weather data:
    {weather_history}

    Temperature is measured in degrees Celsius (°C).
    Humidity is measured in percent (%).
    Wind speed is measured in kilometers per hour (km/h).
    """

    completion = client.chat.completions.create(
        model="cohere/north-mini-code:free",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful weather assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.0
    )

    return completion.choices[0].message.content