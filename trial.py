import requests
	

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

		final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
except:
		final_str = 'There was a problem retrieving that information'

print(final_str)
