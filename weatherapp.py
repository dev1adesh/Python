import requests
import pyttsx3
import json

AI = pyttsx3.init()

print("Welcome to Weather App, created by Adesh Partap Singh")

while True:

    location = input("Enter your location: ")

    if location == 0:
        print("You have exited the program")
        AI.say("You have exited the program")
        AI.runAndWait()
        break
    else:
        location.strip()
        url = f"https://api.weatherapi.com/v1/current.json?key=553752ee1cc44802bf7141530241907&q={location}"

        response = requests.get(url)
        wdic = json.loads(response.text)
        w = wdic["current"]["temp_c"]
        print(w)
        AI.say(f"The current temperature in {location} is {w} degrees celsius")
        AI.runAndWait()
