import requests
import json
class Urlshortener(object):
	def __init__(self):
		self.req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyDGsWyGP19sryyxXCmI3c9abhQYTIu_Iak'
		self.headers = {'content-type': 'application/json'}		

	def get_shorturl(self, content):
		self.payload = {'longUrl': content[2]}
		self.response = requests.post(self.req_url,data = json.dumps(self.payload), headers=self.headers).json()
		return self.response['id']