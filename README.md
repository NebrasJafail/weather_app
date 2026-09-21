# 🌤️ Weather Tracker

A Python and Streamlit weather tracking application that allows users to record, view, search, and analyze weather observations.

The application also integrates an external Weather API to retrieve live weather and a 5-day forecast, and an LLM to generate an AI-powered weather summary.

## 📌 Features

### 📝 Weather Tracking

* Record new weather observations.
* Store observations in a CSV file.
* Load previously recorded observations when the application starts.
* View all recorded observations.
* Search observations by date.

### 📊 Weather Analysis

* Calculate average temperature.
* Find minimum and maximum temperatures.
* Find the most common weather condition.
* Display temperature trends.
* Filter observations by month.
* Filter observations by season.
* Predict tomorrow's weather condition using historical patterns.
* Compare average temperatures between years.
* Identify the highest and lowest recorded temperatures.

### 🌍 External Weather API

The application uses the Open Weather API through RapidAPI.

It provides:

* Live temperature.
* Humidity.
* Wind speed.
* Weather condition.
* 5-day weather forecast.

Live API observations can also be saved automatically to the CSV weather log.

### 🤖 AI Meteorologist

The application integrates an LLM through OpenRouter.

The AI Meteorologist analyzes recent weather observations from the CSV file and generates:

* A natural-language weather summary.
* Temperature and weather-condition observations.
* Practical weather recommendations.

The AI uses the most recent seven calendar days of available weather data.

## 🛠️ Technologies

* Python
* Streamlit
* Pandas
* Requests
* OpenAI Python library
* OpenRouter API
* Cohere model
* RapidAPI
* CSV
* python-dotenv

## 📂 Project Structure

```text
weather-tracker/
│
├── app.py
├── weather_api.py
├── data_manager.py
├── analysis.py
├── ai_meteorologist.py
├── weather_data.csv
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 📄 Python Files

### `app.py`

Contains the Streamlit user interface and connects the different components of the application.

### `weather_api.py`

Handles requests to the external weather API and processes live weather and forecast data.

### `data_manager.py`

Contains functions for loading, saving, and adding weather observations to the CSV file.

### `analysis.py`

Contains functions for weather statistics, trends, filtering, prediction, yearly comparison, and temperature records.

### `ai_meteorologist.py`

Handles the LLM integration through OpenRouter and generates summaries and recommendations from recent weather data.

## 📊 Data Storage

Weather observations are stored in:

`weather_data.csv`

Each observation contains:

* Date
* Temperature (°C)
* Weather condition
* Humidity (%)
* Wind speed (km/h)

## 🔐 API Key Security

API keys are stored in a `.env` file rather than being hardcoded in the Python source code.

The `.env` file is included in `.gitignore` so that API keys are not uploaded to GitHub.

Example:

```text
RAPIDAPI_KEY=your_rapidapi_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

Never share real API keys publicly.

## ⚙️ Installation

Create a virtual environment:

```text
python -m venv .venv
```

Activate the virtual environment on Windows:

```text
.venv\Scripts\Activate.ps1
```

Install the required packages:

```text
python -m pip install -r requirements.txt
```

## 🔑 Environment Setup

Create a `.env` file in the project folder and add your own API keys:

```text
RAPIDAPI_KEY=your_rapidapi_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

Replace the placeholder values with your own keys.

## ▶️ Run the Application

Start the Streamlit application with:

```text
python -m streamlit run app.py
```

The application will open in your web browser.

## 🎯 Project Requirements

This project was developed as part of the General Assembly/Tamkeen Python Fundamentals and API Fundamentals projects.

It demonstrates:

* Python programming fundamentals
* Streamlit application development
* CSV data storage
* Pandas data analysis
* External API integration
* Live weather and forecast data
* LLM API integration
* Environment variable and API key security

## 📚 Learning Resources

The project was developed using official documentation and learning resources for:

- Python
- Streamlit
- Pandas
- Requests
- RapidAPI
- OpenRouter API

Additional learning resources:

- Python - How do I draw a text-based graph of a given function f(x)? - Stack Overflow
https://stackoverflow.com/questions/44067637 how-do-i-draw-a-text-based-graph-of-a-given-function-fx

- The Beginner’s Guide to Language Models with Python
https://machinelearningmastery.com/the-beginners-guide-to-language-models-with-python/


AI assistance was used for learning, debugging, and understanding programming concepts. The code was reviewed and tested to ensure that the project logic and implementation were understood.

AI learning and debugging support:
- https://chatgpt.com/

## 👤 Author

Nebras Jafail
