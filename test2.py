import requests

 
api_key = #api key here
city = 'london'
celsius = 'metric'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units={celsius}&APPID={api_key}'
response = requests.get(url).json()
 
# City
print(response.get('name'))
 
# Temp
print(response['main'].get('temp'))
 
# Description
print(response['weather'][0].get('description'))
 
# Wind
