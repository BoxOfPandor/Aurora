import curses
import json
import random

class IVI:
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
        try:
            with open('responses.json') as f:
                self.responses = json.load(f)
        except FileNotFoundError:
            print("Le fichier 'responses.json' n'a pas été trouvé.")
            self.responses = []

    def interface(self):
        while True:
            self.stdscr.refresh()
            curses.echo()  # Enable echo
            self.stdscr.addstr("User: ")
            user_input = self.stdscr.getstr().decode('utf-8')
            y, x = self.stdscr.getyx()
            curses.noecho()  # Disable echo
            aurora_response = self.get_response(user_input)
            self.stdscr.addstr(y + 1, 0, "Aurora: " + aurora_response)
            self.stdscr.addstr(y + 2, 0, "")
            self.stdscr.refresh()

    def get_response(self, user_input):
        user_input = user_input.lower()
        for response_group in self.responses:
            for phrase in response_group["str_reactant"]:
                if phrase in user_input:
                    return random.choice(response_group["responses"])
        print("response not found")
        return "Je suis désolé, je ne comprends pas."

    def process_data(self, data):
        # Logique pour traiter les données
        pass

    def make_decision(self, processed_data):
        # Logique pour prendre des décisions basées sur les données traitées
        pass

    def __del__(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

ivi = IVI()
ivi.interface()