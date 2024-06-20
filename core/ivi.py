import os
import curses
import json
import random

class IVI:
    def __init__(self):
        try:
            with open('responses.json') as f:
                self.responses = json.load(f)
        except FileNotFoundError:
            print("Le fichier 'responses.json' n'a pas été trouvé.")
            self.responses = []

    def interface(self):
        user_input = input("User: ")
        return user_input

    def make_decision(self, user_input):
        user_input = user_input.lower()
        for response_group in self.responses:
            for phrase in response_group["str_reactant"]:
                if phrase in user_input:
                    return random.choice(response_group["responses"])
        return "Je suis désolé, je ne comprends pas."
    

ivi = IVI()