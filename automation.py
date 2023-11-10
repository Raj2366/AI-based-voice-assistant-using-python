import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...") 

        return "None"
    return query

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",170)




def searchGoogle(query):
    if "search" in query:
        import wikipedia as googleScrap
        query = query.replace("search","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,2)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "play" in query:
        speak("This is what I found for your search!") 
        query = query.replace("play","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")


