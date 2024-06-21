from utils.weather import get_weather, extract_city
from utils.calendar import get_google_calendar_events
import json
import random

class IVI:
    def __init__(self, weather_api_key, calendar_credentials_file):
        self.weather_api_key = weather_api_key
        self.calendar_credentials_file = calendar_credentials_file
        try:
            with open('responses.json') as f:
                self.responses = json.load(f)
        except FileNotFoundError:
            print("Le fichier 'responses.json' n'a pas été trouvé.")
            self.responses = []

    def interface(self):
        user_input = input("User: ")
        return user_input
    
    def process_data(self, text):
        if "météo" in text:
            city = extract_city(text)
            if not city:
                return "Je n'ai pas pu identifier la ville pour la météo."
            return get_weather(self.weather_api_key, city)
        elif "agenda" in text or "événements" in text:
            return get_google_calendar_events(self.calendar_credentials_file)
        else:
            return self.make_decision(text)
        
    def make_decision(self, user_input):
        user_input = user_input.lower()
        for response_group in self.responses:
            for phrase in response_group["str_reactant"]:
                if phrase in user_input:
                    return random.choice(response_group["responses"])
        return "Je suis désolé, je ne comprends pas."
