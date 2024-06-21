import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=fr"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"La météo à {city} est actuellement {weather_description} avec une température de {temperature}°C."
    else:
        return "Je n'ai pas pu obtenir la météo pour " + city

def extract_city(text):
        words = text.split()
        if "météo" in words:
            idx = words.index("météo")
            if idx + 1 < len(words):
                return words[idx + 1]
        return None