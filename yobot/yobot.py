from __future__ import print_function
import zulip
import sys
import pprint
import requests
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
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
		else:
			return

def main():
	bot = Yobot()
	bot.client.call_on_each_message(bot.process_bot)

if __name__ == '__main__':
    main()