from core.ivi import IVI
from core.ava import AVA
from core.eve import EVE

def main():
    ava = AVA()
    ivi = IVI()
    eve = EVE()

    # Exemple d'interaction utilisateur
    voice_data = ava.capture_voice()
    text = ava.convert_voice_to_text(voice_data)
    processed_data = ivi.process_data(text)
    decision = ivi.make_decision(processed_data)
    response_audio = eve.convert_text_to_speech(decision)
    eve.play_response(response_audio)

if __name__ == "__main__":
    main()
