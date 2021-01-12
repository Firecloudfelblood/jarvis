import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes

engine = pyttsx3.init()

months = ["January","February","March","April","May","June","July","August","September","Octuber","November","Dicember"]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    hour = datetime.datetime.now().hour
    if hour > 12:
        ampm = "pm"
        hour -=12
    else:
        ampm ="am"
    min = datetime.datetime.now().minute
    seg = datetime.datetime.now().second

    speak("The current time is" + str(hour)+" "+str(min) +ampm)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is" + str(date) +months[month-1] + str(year))

def wichme():
    speak("welcome back g o")
    time_()
    date_()

    hour = datetime.datetime.now().hour
    if hour >=0 and hour < 12:
        speak("Good morning Sir!")
    elif hour >= 12 and hour <18:
        speak("Good afternoon Sir")
    else:
        speak("Good evening Sir")

    speak("Jarvis at your service. Please tell me how can I help you today?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en_US')
            speak(query)
            print(query)
        except Exception as e:
            print(e)
            print("Say that again please")
            return "None"
        return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('inggyovannycavazos@gmail.com', 'Axl.Vlad.06')
    server.sendmail('inggyovannycavazos@gmail.com', to, content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery = psutil.sensors_battery()
    speak('Batery is at: '+str(battery.percent))

def joke():
    speak(pyjokes.get_joke())

if __name__ == '__main__':
    wichme()

    while True:
        query = TakeCommand().lower()

        if 'time' in query:
            time_()

        elif 'date' in query:
            date_()

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result= wikipedia.summary(query, sentences=3)
            speak("According to wiki pedia")
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should it say")
                content = TakeCommand()
                receiver = 'gyovannycavazosmarquez@gmail.com'
                #
                # speak("Who's the receiver?")
                # receiver = input("Enter the receiver's emal :")

                to = receiver
                sendEmail(to, content)
                speak(content)
                speak('Email has been sent.')

            except Exception as e:
                speak("unable to send email")
                print(e)



        elif 'search in chrome' in query:
            speak("What should I search for?")
            chromepath = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome %s"

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'search youtube' in query:
            speak("What should I search for?")
            search = TakeCommand().lower()
            speak("Here we go to youtube!")
            wb.open('https://www.youtube.com/results?search_query='+search)

        elif 'search google' in query:
            speak("What should I search for?")
            search_Term = TakeCommand().lower()
            speak("Here we go to google")
            speak("Searching....")
            wb.open('https://www.google.com/search?q='+search_Term)

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'go offline' in query:
            speak('Going off line sir!')
            quit()