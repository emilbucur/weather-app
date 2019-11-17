from flask import Flask
from weather import weather
import json


app = Flask(__name__)

@app.route("/")
def Hello():
    return "hello, world!"

@app.route("/weather/")
def vreme():
    temp = weather()
    temp = json.dumps(temp)
    return temp

@app.route("/weather/my-cities/")
def weather_multiple_cities():
    return "Cluj: 15, New York: 10"