import requests
import json
class Hackernews(object):
	def __init__(self):
		self.hack_data = ""
		self.i = 1

	def get_hackernews(self):
		stories_id = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json').json()
		for story_id in stories_id:
			hacker_data = requests.get('https://hacker-news.firebaseio.com/v0/item/' + str(story_id) + '.json?print=pretty').json()
			self.hack_data = self.hack_data + (str(self.i) + '. [' + hacker_data['title'] + '](' + hacker_data['url'] + ')\n')
			self.i = self.i + 1
			if (self.i == 11):
				break
		return self.hack_data