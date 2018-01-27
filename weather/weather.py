import pprint
import requests

p = pprint.PrettyPrinter()
class Weather() :
    def getWeather(self,longAndLat) :
        weatherUrl = 'https://api.darksky.net/forecast/45c3ad46556e3fd3b390a9acd88f664f/'+longAndLat+'/?exclude=minutely,hourly,daily' 
        r=requests.get(weatherUrl)
        result = r.json()
        return result