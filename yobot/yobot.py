import zulip
import pprint
import requests
import os
import json

#initialise pprint
p = pprint.PrettyPrinter()
bot_id = 'yobot-bot@chunkzz.zulipchat.com'
class Yobot(object):
	def __init__(self):
		self.client = zulip.Client(site="https://chunkzz.zulipchat.com/api")
		self.subscribe_streams()

	def subscribe_streams(self):
		all_streams = self.client.get_streams()['streams']
		for stream in all_streams:
			self.client.add_subscriptions([{'name': stream['name']}])

	def process_bot(self, msg):
		print("hithere")
		all_streams = self.client.get_streams()['streams']
		content = msg['content'].split()
		sender_mail = msg['sender_email']
		stream_name = msg['display_recipient']
		stream_topic = msg['subject']
		if sender_mail == bot_id:
			return
		if content[0] == 'yobot' or content[0] == '@**yobot**':
			#motivationak quote
			if content[1] == 'motivate':
				data = requests.get('https://talaikis.com/api/quotes/random/').json()
				self.client.send_message({
    				"type": "stream",
    				"to": stream_name,
    				"subject": stream_topic,
    				"content": '"*' + data['quote'] + '*"\n -by ' + '**' + data['author'] + '**'
				})
			#send mail		
			if content[1] == 'mail':
				mail_data = MIMEText("hii bot")
				mail_data['to'] = 'dagaranupam@gmail.com'
				mail_data['from'] = sender_email
				mail_data['subject'] = "try bot"
				mail_data = (service.users().messages().send(userId=sender_email, body=mail_data).execute())
				print (mail_data['id'])
			#url shortener
			if content[1] == "shortenurl":
				req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyDGsWyGP19sryyxXCmI3c9abhQYTIu_Iak'
				payload = {'longUrl': content[2]}
				headers = {'content-type': 'application/json'}
				response = requests.post(req_url,data = json.dumps(payload), headers=headers).json()
				self.client.send_message({
					"type": "stream",
					"to": stream_name,
					"subject": stream_topic,
					"content": response['id']
					})
			if content[1] == 'hackernews':
				stories_id = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json').json()
				hack_data = ""
				i = 1
				for story_id in stories_id:
					hacker_data = requests.get('https://hacker-news.firebaseio.com/v0/item/' + str(story_id) + '.json?print=pretty').json()
					hack_data = hack_data + (str(i) + '. [' + hacker_data['title'] + '](' + hacker_data['url'] + ')\n')
					i = i + 1
					if (i == 11):
						break
				self.client.send_message({
						"type": "stream",
						"to": stream_name,
						"subject": stream_topic,
						"content": hack_data
						})
		else:
			return

def main():
	bot = Yobot()
	bot.client.call_on_each_message(bot.process_bot)

if __name__ == '__main__':
    main()