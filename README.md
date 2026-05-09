# MOSAM
Mosam is an intelligent weather-based dressing advisor powered by Large Language Models. Instead of just checking the weather, get personalized outfit recommendations based on real-time weather conditions!

## Problem Statement

Weather apps tell you the temperature, humidity, and wind speed—but they don't answer the question that actually matters: *What should I wear?*
Traditional weather apps leave the styling decisions entirely to you. MOSAM bridges that gap by leveraging AI to provide intelligent, context-aware 
clothing recommendations tailored to current weather conditions.

## Features

- **Real-Time Weather Integration**: Fetches current weather data using OpenWeather API
- **AI-Powered Advice**: Uses Groq's LLaMA model for instant, conversational outfit recommendations
- **Multi-Factor Analysis**: Considers temperature, "feels like" temperature, humidity, wind speed, and weather conditions
- **Smart Insights**: Provides three key insights:
  - ***Comfort Level***: Assessment based on temperature and humidity conditions
  - ***Biological Insights***: Health/biological stress factors based on weather
  - ***Energy Level***: Predicted energy/focus potential for the day
- **Data Tracking**: Automatically saves all weather data and AI advice to a local CSV file
- **Easy-to-Use Interface**: Streamlit web app with intuitive input and beautiful metric displays
- **Fast LLM Inference**: Ultra-fast responses using Groq's optimized inference engine

## Tech Stack

- **Language**: Python 3.x
- **Frontend**: Streamlit (web application framework)
- **Weather Data**: OpenWeather API
- **LLM Provider**: Groq (ultra-fast LLM inference)
- **Key Libraries**:
  - `streamlit` - Interactive web app interface
  - `requests` - HTTP requests for weather APIs
  - `groq` - Groq API SDK for LLM queries
  - `pandas` - Data handling and processing

## Requirements

- Python 3.7+
- API keys for:
  - OpenWeather API (for weather data)
  - Groq API (for LLM inference)
- Internet connection for live weather and LLM queries

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/rabailcheema/MOSAM.git
cd MOSAM
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root:
```env
WEATHER_API_KEY=your_openweather_api_key
GROQ_API_KEY=your_groq_api_key
```

Get your API keys:
- **OpenWeather API**: [openweathermap.org](https://openweathermap.org/api)
- **Groq API**: [console.groq.com](https://console.groq.com)

## Usage

### Run the Streamlit App
```bash
streamlit run main.py
```

The app will open in your default browser at `http://localhost:8501`

### How to Use
1. **Enter City Name**: Type the city you want weather for (e.g., "Islamabad", "New York")
2. **Optional Country Code**: Add a country code for more accurate results (e.g., "PK" for Pakistan, "US" for USA)
3. **Click "Get Weather"**: Submit your request
4. **View Results**:
   - Temperature and "feels like" metrics
   - Current weather condition and wind speed
   - **Comfort Insight**: How comfortable the weather is
   - **Bio Insight**: Biological/health factors to consider
   - **Energy Level**: Your predicted productivity/energy for the day
   - **AI Advice**: Conversational recommendation from Groq's AI


## API Configuration

### Weather API
Uses OpenWeather API for real-time weather data.
- Get a free API key at [openweathermap.org](https://openweathermap.org/api)
- Free tier includes current weather, forecasts, and more

### Groq LLM
Provides ultra-fast LLM inference for outfit recommendations.
- Sign up at [console.groq.com](https://console.groq.com)
- Get your API key from the dashboard
- Free tier available with generous rate limits
- Uses **LLaMA 3.1 8B Instant** model for fast, conversational responses
- Supports fallback to rule-based advice if API fails

## How It Works

1. **User Input**: Enter city name and optional country code in the Streamlit interface
2. **Weather Data Retrieval**: Fetches real-time data from OpenWeather API using the city location
3. **Data Processing**: Extracts temperature, humidity, wind speed, pressure, and weather conditions
4. **AI Advice Generation**: 
   - Sends weather context to Groq's LLaMA 3.1 model
   - Gets conversational advice about what to wear and what to do
   - Falls back to simple rules-based advice if API fails
5. **Insight Calculations**: Analyzes conditions to provide comfort assessment based on temperature/humidity combinations
6. **Beautiful Display**: Shows metrics, conditions, and AI advice in an easy-to-read format
7. **Data Persistence**: Automatically saves all data to `weather_data_with_ai.csv` for history tracking

## Project Structure

```
MOSAM/
├── main.py              # Streamlit app entry point
├── requirements.txt     # Python dependencies
├── .env.example        # Example environment variables
├── .gitignore          # Git ignore file
└── README.md           # This file
```

**main.py** contains:
- Streamlit UI configuration
- Weather API integration
- Groq LLM queries
- Outfit recommendation logic

## Deployment

### Deploy on Streamlit Cloud

1. **Push to GitHub**: Ensure your repository is public on GitHub
2. **Go to Streamlit Cloud**: Visit [share.streamlit.io](https://share.streamlit.io)
3. **Connect Repository**: Sign in with GitHub and select your repository
4. **Configure Secrets**: Add your API keys in the "Secrets" section
5. **Deploy**: Click deploy and your app will be live!

### Environment Variables for Deployment
In Streamlit Cloud, go to **Settings** → **Secrets** and add:
```
WEATHER_API_KEY = "your_openweather_api_key"
GROQ_API_KEY = "your_groq_api_key"
```

## Contributing

Contributions are welcome! Here are ways you can help:

1. **Report Bugs**: Found an issue? Open a GitHub issue
2. **Suggest Features**: Have ideas? Share them in discussions
3. **Improve Code**: Submit pull requests with improvements
4. **Add Support**: Extend LLM provider support or add new weather APIs

### Development Setup
```bash
git clone https://github.com/rabailcheema/MOSAM.git
cd MOSAM
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Troubleshooting

### "API keys not found. App will not fetch live data."
- Ensure your `.env` file is in the same directory as `main.py`
- Check that both `WEATHER_API_KEY` and `GROQ_API_KEY` are set
- If deployed on Streamlit Cloud, add them to **Settings** → **Secrets**, not as GitHub secrets

### "Invalid API Key" Error
- Verify your API keys are correct and active
- Check that your keys haven't expired or been rotated
- Ensure you haven't exceeded API rate limits

### "City not found" Error
- Try using a more specific city name with country code (e.g., "Islamabad, PK")
- Some smaller cities may not be in the database; try a nearby major city

### Slow Response / Timeout
- Check your internet connection
- Verify Groq API is accessible at [console.groq.com](https://console.groq.com)
- The free tier has rate limits; try again after a brief wait

### CSV File Not Being Created
- Ensure the app has write permissions in its directory
- Check that `weather_data_with_ai.csv` isn't corrupted or locked by another program
- Try running the app from a directory with full write access

### "No such module" Error
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify you're using Python 3.7 or higher: `python --version`
- Consider using a virtual environment to avoid dependency conflicts

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Rabail Inshra Cheema**  
GitHub: [@rabailcheema](https://github.com/rabailcheema)

## Support

If you found MOSAM helpful, please consider giving it a star! Your support motivates continued development.

## Contact & Support

For questions, suggestions, or issues:
- Open a [GitHub Issue](https://github.com/rabailcheema/MOSAM/issues)
- Reach out via GitHub discussions
