# Create the guessing game with this dictionary of countries and their capitals.
import random

COUNTRIES_CAPITALS_DICTIONARY = {
    "Afghanistan": "Kabul",
    "Armenia": "Yerevan",
    "Australia": "Canberra",
    "Austria": "Vienna",
    "Belgium": "Brussels",
    "Canada": "Ottawa",
    "China": "Beijing",
    "Cuba": "Havana",
    "Denmark": "Copenhagen",
    "Egypt": "Cairo",
    "Ethiopia": "Addis Ababa",
    "Finland": "Helsinki",
    "India": "New Delhi",
    "Iraq": "Baghdad",
    "Italy": "Rome",
    "Kenya": "Nairobi",
    "Lebanon": "Beirut",
    "Poland": "Warsaw",
    "Russia": "Moscow",
    "South Korea": "Seoul",
    "Vietnam": "Hanoi",
}

# Write the rest of your code here!

true = True
false = False

usrpoint = 0
while true:
    usrpoint += 1 if (input("What is the capital of " + list(COUNTRIES_CAPITALS_DICTIONARY.keys())[random.randint(0, len(COUNTRIES_CAPITALS_DICTIONARY) - 1)] + "?\n") in COUNTRIES_CAPITALS_DICTIONARY.values()) else 0 if print("Wrong!") is None else 0
    print("Points: " + str(usrpoint))


