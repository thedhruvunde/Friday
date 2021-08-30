import json
from urllib.request import urlopen
try:
    jsonObj = urlopen('''https://newsapi.org/v2/articles?source=the-times-of-india&sortBy=top&apiKey=46f67483cd6a40a8a86ffc784bdb6fdd''')
    data = json.load(jsonObj)
    i = 1
     
    print('here are some top news from the times of india')
    print('''=============== TIMES OF INDIA ============'''+ '\n')
     
    for item in data['articles']:
         
        print(str(i) + '. ' + item['title'] + '\n')
        print(item['description'] + '\n')
        print(str(i) + '. ' + item['title'] + '\n')
        i += 1
except Exception as e:
    print(str(e))