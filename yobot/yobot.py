import zulip
import pprint
import requests
import os
import json
from motivate import Motivate
from shorturl import Urlshortener
from hackernews import Hackernews
#initialise pprint
p = pprint.PrettyPrinter()
bot_id = 'yobot-bot@chunkzz.zulipchat.com'

class Yobot(object):
	def __init__(self):
		self.client = zulip.Client(site="https://chunkzz.zulipchat.com/api")
		self.motivate = Motivate()
		self.shortenedurl = Urlshortener()
		self.hacknews = Hackernews()
		self.subscribe_streams()

	def subscribe_streams(self):
		all_streams = self.client.get_streams()['streams']
		for stream in all_streams:
			self.client.add_subscriptions([{'name': stream['name']}])

	def process_bot(self, msg):
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
				quote_data = self.motivate.get_quote()
				self.client.send_message({
					"type": "stream",
					"to": stream_name,
					"subject": stream_topic,
					"content": quote_data
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
				short_url = self.shortenedurl.get_shorturl(content)
				self.client.send_message({
					"type": "stream",
					"to": stream_name,
					"subject": stream_topic,
					"content": short_url
					})

			#hackernews
			if content[1] == 'hackernews' or content[1] == 'hn' or content[1] == 'HN':
				news = self.hacknews.get_hackernews()
				self.client.send_message({
						"type": "stream",
						"to": stream_name,
						"subject": stream_topic,
						"content": news
						})
		else:
			return

def main():
	bot = Yobot()
	bot.client.call_on_each_message(bot.process_bot)

if __name__ == '__main__':
    main()