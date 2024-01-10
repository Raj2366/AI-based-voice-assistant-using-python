import pyttsx3
import speech_recognition
import datetime
import wikipedia
import webbrowser
import requests
import os
import openai
from config import apikey
from gui import play_gif


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


chatStr = ""


def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Raj: {query}\n Saviour: "
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    speak(response.choices[0].text)
    chatStr += f"{response.choices[0].text}\n"
    return response.choices[0].text


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response.choices[0].text
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)


def wishMe():
    play_gif
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    elif hour >= 18 and hour < 20:
        speak("Good Evening!")

    else:
        speak("Good Night!")

    speak("Hi, I am your info assistant. please tell me how may i help you ")


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        print("Recognizing....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again please...")

        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("search wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Ok boss")
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            speak("Ok boss")
            webbrowser.open("google.com")

        elif 'commands list' in query:
            speak("my commands are")
            speak("you can say open google")
            speak("you can say open youtube")
            speak("you can ask time")
            speak("you can say search wikipedia related any topic")
            speak("you can ask the latest news")
            speak("you can say search any topic on google")
            speak("you can say play any video on youtube")
            speak("you can ask weather")
            speak("you can hear the facts")
            speak("you can say exit when your search is done")
            speak("you can give your feedback")



        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"the time is {strTime}")
            speak(f"the time is {strTime}")


        elif 'date' in query:
            str_date = datetime.datetime.now().strftime("%d-%m-%Y")
            print(f"the time is {str_date}")
            speak(f"the date is {str_date}")


        elif "search" in query:
            from automation import searchGoogle

            searchGoogle(query)

        elif "play" in query:
            from automation import searchYoutube

            searchYoutube(query)


        elif "latest news" in query:

            """from newsread import latestnews
            latestnews()"""
            from apikey import *

            arr = news()
            # webbrowser.open("http://127.0.0.1:5500/news%20api.html")
            print("Ok , Now I will read news for you")
            speak("Ok , Now I will read news for you")
            for i in range(len(arr)):
                print(arr[i])
                speak(arr[i])





        elif "weather" in query:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        # elif 'exit' in query:
        # exit()

        # elif 'facts' in query:
        # a= randfacts.getFact()

        # print(a)
        # speak("did you know that, "+a)

        # elif 'using artificial intelligence'.lower() in query.lower():

        elif 'feedback' in query:
            speak("It is my pleasure to take the feedback from you")
            #webbrowser.open("http://localhost/information/index.php")
            speak("please give your feedback")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "exit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)

#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