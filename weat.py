from weather import Weather, Unit
weather = Weather(unit=Unit.CELSIUS)
t=input("Enter your Location:")
location=weather.lookup_by_location(t)
forecasts = location.forecast
print('text'+'|'+'date'+'|'+'high'+'|'+'low')
for forecast in forecasts:
	print(forecast.text+'|'+forecast.date+'|'+forecast.high+'|'+forecast.low)
