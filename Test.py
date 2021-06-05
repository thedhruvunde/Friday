import webbrowser as web
import os

def speak(audio):
    print(audio)

def takeCommand():
    query = input("Type Here> ")
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        
        if 'play' in query:
            query = query.split(' ')
            query.remove('play')
            query.remove('songs')
            songDir = "C:\\Users\\DELL\\Music\\"
            for v in range(0, len(query), 1):
            	songDir += str(query[v])
            songs = os.listdir(songDir)
            os.startfile(os.path.join(songDir, songs[0]))