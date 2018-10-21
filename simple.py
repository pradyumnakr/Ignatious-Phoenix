from flask import Flask, redirect, url_for, request
import geocoder
import requests
from weather import Weather, Unit
from flask import Flask, render_template, jsonify, request, redirect, url_for
app=Flask(__name__, template_folder='templates')

@app.route('/success/<name>')
def success(name):
   h=name
   g=geocoder.osm(h)
   t=str(g.latlng)
   return str('Your Location is:'+t)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@app.route('/weather_info', methods=['POST'])
def weather_info():
    city_input = request.form["weather"]
    # Setup OpenWeatherMap API
    api_key = '3ad42b95721c61094d1dff3f1fe8ba1d'    
    celsius = 'metric'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_input}&units={celsius}&APPID={api_key}'
    response = requests.get(url).json()    
    # API get data
    try:
        city = response['name']
        temp = response['main']['temp']
        description = response['weather'][0]['description']
        wind = response['wind']['speed']
    except KeyError:
        return redirect(url_for('error'))
    return render_template('weatherloc.html', city=city, temp=temp, description=description, wind=wind)


