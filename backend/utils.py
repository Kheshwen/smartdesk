import requests
from config import WEATHER_API_KEY, NEWS_API_KEY

def get_weather(city='Kuala Lumpur'):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    res = requests.get(url).json()
    return {
        'city': city,
        'temperature': res['main']['temp'],
        'description': res['weather'][0]['description']
    }

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=my&apiKey={NEWS_API_KEY}"
    res = requests.get(url).json()
    return res['articles'][:5]

def get_quote():
    try:
        res = requests.get("https://zenquotes.io/api/random").json()
        return res[0]["q"] + " - " + res[0]["a"]
    except:
        return "Stay positive, work hard, make it happen."
