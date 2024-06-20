from core.ivi import IVI
from core.ava import AVA
from core.eve import EVE

def main():
    ava = AVA()
    ivi = IVI()
    eve = EVE()

    while True:
        user_input = ivi.interface()
        data = ava.process_input(user_input)
        processed_data = eve.process_data(data)
        decision = ivi.make_decision(processed_data)
        print(decision)

if __name__ == "__main__":
    main()
