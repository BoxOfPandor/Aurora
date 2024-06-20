from gtts import gTTS
import pygame
import os

class EVE:
    def __init__(self):
        # Initialisation du Core EVE
        pygame.mixer.init()

    def convert_text_to_speech(self, text, lang='fr'):
        tts = gTTS(text=text, lang=lang)
        tts.save("response.mp3")

    def play_response(self):
        pygame.mixer.music.load("response.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        os.remove("response.mp3")