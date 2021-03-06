import os
import pyttsx3
import speech_recognition as sr
import datetime
import smtplib
import webbrowser as web
import wikipedia
import pyjokes
import wolframalpha
import random
import string
import requests


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        with open(".Errors.log", 'a') as f:
            f.write(str(e)+'\n') 
        speak("Say that again please...")  
        return "None"
    return query

def takeConsoleCommand():
    query = str(input("Type here> "))
    return query

def getWheather():
    weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
    city = 'pune'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        return desc
        return temp
            #speak(f"Sir, the Temperature in the city is {temp} degree celcius and climate is {desc}")
    except:
        pass
def wishMe():
    hour = int(datetime.datetime.now().hour)
    getWheather()
    if hour>=0 and hour<12:
        speak(f"Good Morning Boss!, today's wheather is {desc} and temperature is {temp} degree celcius")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss!")   

    else:
        speak("Good Evening Boss!")  

    speak("Please tell me how may I help you")

def sendEmail(to, content, passwd):
    if passwd == 'dhruv2609':
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.login('dhruvunde26@gmail.com', passwd)
        server.sendmail('dhruvunde26@gmail.com', to, content)
        server.close()

def PasswdGenerator(pass_str, pass_len):
    password = ''
    speak("Generating Password...")
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str = password
    speak("Password Generated!")
    print(f"Password: {pass_str}")

def Cands(cand):
    recv = {
        'mother':'dhruvpradnya@gmail.com',
        'code':'dhruvcode413@gmail.com',
        'yash mulay':'sm.mulay2015@gmail.com'
    }
    if cand in recv:
        recp = recv[cand]
        return recp
    else:
        speak("Contact not found in contact list, type email address")
        recp = input("Type Here> ")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'search' in query:
            try:
                search = query.split(' ')
                search.remove('search')
                search.remove('on')
                if 'youtube' in search:
                    speak("OK, Searching Youtube!")
                    result = "youtube.com/results?search_query="
                    for j in range(0, len(search), 1):
                        result = result + '+' + search[j]
                    speak("Here are the results!")
                    web.open(result)
                if 'google' in search:
                    speak("OK, Searching Google!")
                    result = "https://www.google.com/search?q="
                    for j in range(0, len(search), 1):
                        result = result + '+' + search[j]
                    speak("Here are the results!")
                    web.open(result)
                if 'github' in search:
                    speak("OK, Searching Github!")
                    result = "https://github.com/search?q="
                    for j in range(0, len(search), 1):
                        result = result + search[j] + '+' 
                    speak("Here are the results!")
                    web.open(result)
                if 'wikipedia' in search:
                    speak("OK, Searching Wikpedia!")
                    result = ""
                    for j in range(0, len(search), 1):
                        result = result + ' ' + search[j]
                    wiki = wikipedia.summary(result, sentences=2)
                    speak('According to Wikipedia...')
                    speak(wiki)   
                if 'stackoverflow' in search:
                    speak("OK, Searching StackOverflow!")
                    result = "https://stackoverflow.com/search?q="
                    for j in range(0, len(search), 1):
                        result = result + '+' + search[j]
                    speak("Here are the results!")
                    web.open(result)         
            except Exception as s:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Boss, the time is {strTime}")
        
        elif 'the date' in query:
            strDate = str(datetime.date.today())
            speak(f"Boss, the date is {strDate}")
        
        elif 'execute' in query:
            query = query.replace('open', '')
            query = query.replace('execute', '')
            speak('OK, executing '+query)
            os.system(query)

        elif 'email' in query:
            try:
                speak('To whom?')
                to = takeCommand()
                Cands(to)
                speak("What should I say?")
                content = takeCommand()  
                speak("You have to enter Password to login...")
                passwd = input('passwd> ')
                sendEmail(to, content, passwd)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Boss. I am not able to send this email")
        
        elif 'open' in query:
            query = query.split(' ')
            query.remove('open')
            count = 0
            result = str(None)
            while (count<len(query)):
                result += query[count] + ' '
                count += 1
            if 'command' in result:
                os.system("cmd")

            elif 'browser' in result:
                web.open("")
        
            elif 'github' in result:
                web.open("github.com")

            elif 'file' in result:
                os.system("nautilus")

            elif 'visual studio' in result:
                os.system("code")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:
        
            app_id = "G7RL9K-3PRAHV2PA8"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            speak("The answer is " + answer)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("Here are the result")
            web.open("https://www.google.nl / maps / place/" + location + "")

        elif "Thank You" in query:
            speak("It's my pleasure")

        elif "exit" in query:
            speak("Are you sure?")
            ans = takeCommand()
            if 'yes' in ans:
                exit()
            else:
                pass

        elif "shutdown" in query:
            speak("Okay, powering off...")
            os.system("shutdown now")

        elif "reboot" in query:
            speak("Okay, rebooting the computer...")
            os.system("reboot")
        
        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i want to type" in query:
            speak("Okay!")
            query = takeConsoleCommand().lower()

        elif "i want to talk" in query:
            speak("Okay!")
            query = takeCommand().lower()
 
        elif "open camera" in query:
            os.system("cheese")

        elif "generate password" in query:
            pass_str = ""
            speak("Please enter length of password...")
            pass_len = int(takeCommand())
            PasswdGenerator(pass_str, pass_len)

        elif "simulate dice" in query:
            dice_num = random.randint(1, 6)
            speak("Starting simulation...")
            speak(dice_num)
        
        elif "weather" in query:
             
            getWheather()
            speak(f"Boss, Today's wheather is {desc} and temperature is {temp} degree celcius")