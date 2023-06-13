import pyttsx3  # pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia # pip install wilipedia
import webbrowser
import smtplib
# pip install PyAudio


engine = pyttsx3.init('sapi5')  #sapi5 for taking voice
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id) #for setting the engine voice


def speak(audio):
    engine.say(audio) #audio string ko engine bolega
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour) #for getting time from 0 to 24 hour
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am jarvis sir..Please tell me how may i help you")

def takeCommand(): #it takes microphone input from the user and returns string output
    r = sr.Recognizer() #it will help us to recognize the audio
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # for giving time during speaking, 1 means for giving 1 sec,agar mai kuch bol rha hu to agar thoda mai samay le leta hu to kahi ye us baat ko complete na kar de isliye 1 sec ka pause time liye hai
        audio = r.listen(source)  # ye sb speechrecogination wale module se aa rhe hai
    
    try:
        print("Recognizing...") #commond ko recognize karega
        query = r.recognize_google(audio, language='en-in') #en-in means english India, recognixe_google means it is using google engine for heraing voice or recognizing voice
        print(f"User said: {query}\n") #audio recnige karenge jo audio type ki gyi hai
        #install PyAudio otherwise takcommand won't work..

    except Exception as e:
        print(" Please say that again couldn't hear clearly....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('alirahmat7909@gmail.com', 'rahmat@3364')
    server.sendmail('alirahmat7909@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    #while True: # it will listen continusly
    if 1:  # it will listen only one because we took 1...
        query = takeCommand().lower()
        #now writing logic for executing tasks based on query below
        if 'wikipedia' in query:
            speak('Searching Wikipedis..please wait')
            query = query.replace("Wilipedia", "") #replace with blank  means wilipedia hata dunga mai
            results = wikipedia.summary(query, sentences=2) # sentences=2 means it will return 2 sentences from wilipedia
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:  # query k unsder youtube hai to ye youtube ko kholega,youtube ko kholne kiye hum log ko webbrowser install karna padta hai jo ki inbult hai pehle se hi
            webbrowser.open("youtube.com")
      
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stactoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        elif 'email to sam' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "alirahmat@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend rahmat bro, I am not able to send this email because you couldn't enable less secure app in your gmail")

        elif 'best friend' in query:
            speak("Ayan is your best friend rahmat sir")



