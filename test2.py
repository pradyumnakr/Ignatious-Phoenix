import requests
 
# Call example
#http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&APPID=3ad42b95721c61094d1dff3f1fe8ba1d
 
api_key = '3ad42b95721c61094d1dff3f1fe8ba1d'
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
