import streamlit as st
import requests
import pandas as pd
from groq import Groq
import os

# API KEYS
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Validate keys
if not WEATHER_API_KEY or not GROQ_API_KEY:
    st.warning("API keys not found. App will not fetch live data.")
    st.stop()

# Configure Groq
client = Groq(api_key=GROQ_API_KEY)

# Title
st.title("MOSAM")
st.write("Get weather insights + AI-powered advice")

# User Input
city = st.text_input("Enter your city")
country = st.text_input("Country code (optional, e.g. PK, US)").upper()

# AI Advice
def get_ai_advice(record):
    prompt = f"""You are a friendly weather assistant. Based on this weather data, give brief, practical advice:

Weather in {record['city']}:
- Temperature: {record['temperature']}°C (feels like {record['feels_like']}°C)
- Humidity: {record['humidity']}%
- Condition: {record['weather']}
- Wind speed: {record['wind_speed']} m/s

Provide 2-3 sentences of natural, conversational advice about what to wear and do."""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=0.4,
            max_tokens=150,
            messages=[
                {"role": "system", "content": "You are a helpful weather advisor."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()

    except Exception:
        return get_simple_advice(record)

# Fallback
def get_simple_advice(record):
    advice = []
    temp = record['temperature']
    humidity = record['humidity']
    weather = record['weather'].lower()

    if temp > 35:
        advice.append("Very hot. Stay hydrated.")
    elif temp < 10:
        advice.append("Cold. Wear warm clothes.")
    else:
        advice.append("Moderate. Dress comfortably.")

    if "rain" in weather:
        advice.append("Carry an umbrella.")

    if humidity > 75:
        advice.append("Drink water regularly.")

    return " ".join(advice)


def comfort_insight(temp, humidity):
    if temp > 35 and humidity > 70:
        return "Oppressive heat. Expect fatigue."
    elif 20 <= temp <= 28:
        return "Comfortable conditions."
    elif temp < 10:
        return "Cold. Low energy likely."
    return "Moderate conditions."

def bio_insight(temp, humidity):
    if humidity > 80:
        return "High humidity may support microbial growth."
    if temp > 35:
        return "Heat increases dehydration stress."
    return "No major biological stress."

def energy_level(temp, humidity):
    if temp > 32 and humidity > 70:
        return "Low energy day."
    if 20 <= temp <= 27:
        return "High focus potential."
    return "Moderate energy."

# Fetch weather
def fetch_weather(city, country):
    query = f"{city},{country}" if country else city
    url = f"https://api.openweathermap.org/data/2.5/weather?q={query}&appid={WEATHER_API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return None, data.get("message", "Error")

    record = {
        "city": data.get('name', city),
        "temperature": data['main']['temp'],
        "humidity": data['main']['humidity'],
        "pressure": data['main']['pressure'],
        "wind_speed": data['wind']['speed'],
        "weather": data['weather'][0]['description'],
        "feels_like": data['main'].get('feels_like'),
        "country": data.get('sys', {}).get('country', '')
    }

    return record, None

# Button trigger
if st.button("Get Weather"):

    if not city:
        st.warning("Please enter a city")
        st.stop()

    record, error = fetch_weather(city, country)
    

    if error:
        st.error(error)
        st.stop()

    # AI Advice
    advice = get_ai_advice(record)

    # INSIGHTS 
    
    comfort = comfort_insight(record["temperature"], record["humidity"])
    bio = bio_insight(record["temperature"], record["humidity"])
    energy = energy_level(record["temperature"], record["humidity"])

    # Display
    st.subheader(f"{record['city']}, {record['country']}")

    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", f"{record['temperature']}°C")
    col2.metric("Feels Like", f"{record['feels_like']}°C")
    col3.metric("Humidity", f"{record['humidity']}%")

    st.write(f"**Condition:** {record['weather'].capitalize()}")
    st.write(f"**Wind Speed:** {record['wind_speed']} m/s")

    # Advice Box
    st.markdown("### Insights")

    st.write("Comfort:", comfort)
    st.write("Bio:", bio)
    st.write("Energy:", energy)

    st.markdown("### Advice")
    st.success(advice)

    # Save
    record["ai_advice"] = advice
    df = pd.DataFrame([record])

    file_path = "weather_data_with_ai.csv"
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, index=False)

    st.caption("Data saved locally")