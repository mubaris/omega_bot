import pprint
import requests

p = pprint.PrettyPrinter()
class Geocode() :
    def convert(self,place) :
        url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' +place+ ',+CA&key=AIzaSyBKmBYERZyz9Cj7-F9bT7WMWVuSHiaX9kU'
        r = requests.get(url)
        results = r.json()
        longitude = results["results"][0]["geometry"]["location"]["lat"]
        latitude = results["results"][0]["geometry"]["location"]["lng"]
        return str(latitude)+','+str(longitude)
        




