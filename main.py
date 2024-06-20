from core.ivi import IVI
from core.ava import AVA
from core.eve import EVE

def main():
    ava = AVA()
    ivi = IVI()
    eve = EVE()

    while True:
        user_input = ivi.interface()
        if user_input.lower() == "exit":
            break
        aurora_response = ivi.make_decision(user_input)
        print("Aurora: " + aurora_response + "\n")

if __name__ == "__main__":
    main()
