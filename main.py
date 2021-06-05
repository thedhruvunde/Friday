import pyttsx3
import speech_recognition as sr
import datetime
import smtplib
import webbrowser as web
import wikipedia
import os

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
            f.write(e+'\n') 
        speak("Say that again please...")  
        return "None"
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss!")   

    else:
        speak("Good Evening Boss!")  

    speak("I am Friday. Please tell me how may I help you")

def sendEmail(to, content, passwd):
    if passwd == 'dhruv2609':
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.login('dhruvunde26@gmail.com', passwd)
        server.sendmail('dhruvunde26@gmail.com', to, content)
        server.close()

def Cands(cand):
    Candidiates = {
        'mother':'dhruvpradnya@gmail.com',
        'code':'dhruvcode413@gmail.com'
    }
    candid = Candidiates[cand]
    return candid

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'search for' in query:
            try:
                search = query.split(' ')
                search.remove('search')
                search.remove('for')
                search.remove('on')
                if 'youtube' in search:
                    speak("OK, Searching Youtube!")
                    result = "youtube.com/results?search_query="
                    for j in range(0, len(search)-1, 1):
                        result = result + '+' + search[j]
                    web.open(result)
                if 'google' in search:
                    speak("OK, Searching Google!")
                    result = "https://www.google.com/search?q="
                    for j in range(0, len(search)-1, 1):
                        result = result + '+' + search[j]
                    web.open(result)
                if 'github' in search:
                    speak("OK, Searching Github!")
                    result = "https://github.com/search?q=user%3Adhruvcode413+"
                    for j in range(0, len(search)-1, 1):
                        result = result + '+' + search[j]
                    web.open(result)
                if 'wikipedia' in search:
                    speak("OK, Searching Wikpedia!")
                    result = ""
                    for j in range(0, len(search)-1, 1):
                        result = result + ' ' + search[j]
                    wiki = wikipedia.summary(result, sentences=2)
                    speak('According to Wikipedia...')
                    speak(wiki)   
                if 'stackoverflow' in search:
                    speak("OK, Searching StackOverflow!")
                    result = "https://stackoverflow.com/search?q="
                    for j in range(0, len(search)-1, 1):
                        result = result + '+' + search[j]
                    web.open(result)         
            except Exception as s:
                speak("Search not recognized...")
                pass

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Boss, the time is {strTime}")
        
        elif 'the date' in query:
            strDate = str(datetime.date.today())
            speak(f"Boss, the date is {strDate}")
        
        elif 'execute' in query:
            query = query.replace('open', '')
            speak('OK, opening '+query)
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
                #print(e)
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
                os.system("cmd.exe")
            
            elif 'code' in result:
                os.system("code")

            elif 'browser' in result:
                os.startfile("C:\\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
            
            elif 'sublime' in result:
                os.startfile("C:\\Program Files (x86)\Sublime Text 3\sublime_text.exe")
            
            elif 'visual studio' in result:
                os.startfile("C:\\Program Files (x86)\Microsoft Visual Studio\\2019\Community\Common7\IDE\devenv.exe")
            
            elif 'kali' in result:
                os.system("wsl -d kali-linux")
            
            elif 'github' in result:
                os.startfile("C:\\Users\DELL\AppData\Local\GitHubDesktop\GitHubDesktop.exe")
            
            elif "zoom" in result:
                os.startfile("C:\\Users\DELL\AppData\Roaming\Zoom\\bin\Zoom.exe")

            elif 'excel' in result:
                os.startfile("C:\\Program Files\Microsoft Office\\root\Office16\EXCEL.exe")
            
            elif 'access' in result:
                os.startfile("C:\\Program Files\Microsoft Office\\root\Office16\MSACCESS.exe")
            
            elif 'publisher' in result:
                os.startfile("C:\\Program Files\Microsoft Office\\root\Office16\MSPUB.exe")
            
            elif 'one note' in result:
                os.startfile("C:\\Program Files\Microsoft Office\\root\Office16\ONENOTE.exe")
            
            elif 'outlook' in result:
                os.startfile("C:\\Program Files\Microsoft Office\\root\Office16\OUTLOOK.exe")
            
            elif 'powerpoint' in result:
                os.startfile("C:\\Program Files\Microsoft Office\\root\Office16\POWERPNT.exe")
            
            elif 'visio' in result:
                os.startfile("C:\\Program Files\Microsoft Office\\root\Office16\VISIO.exe")
            
            elif 'project' in result:
                os.startfile("C:\\Program Files\Microsoft Office\\root\Office16\WINPROJ.exe")
            
            elif 'word' in result:
                os.startfile("C:\\Program Files\Microsoft Office\\root\Office16\WINWORD.exe")
            
            elif 'photoshop' in result:
                os.startfile("D:\\Photoshop Files\Photoshop Files\Photoshop.exe")
            
            elif 'whatsapp' in result:
                os.startfile("C:\\User\DELL\AppData\Local\WhatsApp\WhatsApp.exe")

        el