import requests
import json
import pyttsx3
import speech_recognition



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",170)

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
        n= int(query)
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again please...") 

        return "None"
    return query


api_address = "https://newsapi.org/v2/top-headlines?country=in&apiKey=c65745a42f1748929f6091fa31907940"

json_data = requests.get(api_address).json()

ar = []

def news():
    
    speak("how many headlines you want to listen")
    #speak("please enter the no.")
    
    query = takeCommand()
    n= int(query)
    for i in range(int(n)):
        ar.append("Number" + str(i+1)+"," + json_data["articles"][i]["title"]+".")
    return ar
    
        


     
     

     


    

    

    
    

         

    
         
    
    


    


     

         
        

    
    
    

    
        
        
    
'''speak("for continue the news say yes")
if 'yes' in query:
    pass
elif'no' in query:
    break'''
         
    


                  
          
  
               
               




     


     




          