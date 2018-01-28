import requests
class Motivate(object):
	def __init__(self):
		self.data = requests.get('https://talaikis.com/api/quotes/random/').json()

	def get_quote(self):
		return "\"*" + self.data['quote'] + '*"\n -by ' + '**' + self.data['author'] + '**'
