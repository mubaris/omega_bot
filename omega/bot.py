import pprint
import zulip
import sys
import re
import json
from crypto import Crypto
from chatterbot import ChatBot
from translate import Translate
from giphy import Giphy
from wiki import WikiPedia
from twitter import Twimega
from motivate import Motivate
from shorturl import Urlshortener
from hackernews import Hackernews
from geocode import Geocode
from weather import Weather 
from dict_ import Dictionary
from joke import Joke
from pnr import Pnr
from mustread import Mustread
from screenshot import Ss
from poll import Poll

p = pprint.PrettyPrinter()
BOT_MAIL = "chunkzz-bot@chunkzz.zulipchat.com"

class ZulipBot(object):
	def __init__(self):
		self.client = zulip.Client(site="https://chunkzz.zulipchat.com/api/")
		self.subscribe_all()
		self.chatbot = ChatBot("Omega", trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
		self.chatbot.train("chatterbot.corpus.english")
		self.crypto = Crypto()
		self.trans = Translate()
		self.g = Giphy()
		self.w = WikiPedia()
		self.tw = Twimega()
		self.motivate = Motivate()
		self.shortenedurl = Urlshortener()
		self.hacknews = Hackernews()
		self.geo = Geocode()
		self.weather = Weather()
		self.dict_ = Dictionary()
		self.joke = Joke()
		self.pnr = Pnr()
		self.mustread = Mustread()
		self.ss = Ss()
		self.poll = Poll()
		self.subkeys = ["crypto", "translate", "define", "tell", "weather", 
				"giphy", "pnr", "mustread", "poll", "hackernews", "hn", "HN", "motivate",
				"twitter"]

	def urls(self, link):
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', link)
		return urls

	def subscribe_all(self):
		json = self.client.get_streams()["streams"]
		streams = [{"name": stream["name"]} for stream in json]
		self.client.add_subscriptions(streams)

	def process(self, msg):
		content = msg["content"].split()
		sender_email = msg["sender_email"]
		ttype = msg["type"]
		stream_name = msg['display_recipient']
		stream_topic = msg['subject']

		print(content)

		if sender_email == BOT_MAIL:
			return 

		print("yeah")

		if content[0] == "omega" or content[0] == "@**omega**":
			if content[1] == "crypto":
				if len(content) > 3 and content[3] == "in":
					message = self.crypto.get_price(content[2], content[4])
				else:
					message = self.crypto.get_price(content[2])
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": message
					})
			if content[1] == "translate":
				ip = content[2:]
				ip = " ".join(ip)
				message = self.trans.translate(ip)
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": message
					})
			if content[1] == "define":
				word = content[2]
				result = self.dict_.words(word)
				print(result)
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": "**"+word+" means :"+"**"+'\n'+result  
					})
			if content[1] == "tell" and content[2] == "a" and content[3] == "joke":
				text = self.joke.tellJoke()
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": text  
					})
			if content[1] == "weather":
				place = " ".join(content[2:])
				result = self.weather.getWeather(self.geo.convert(place))			
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": "**"+"Weather update of "+place+"**"+"\n"+"Summary : " + "**"+result["currently"]["summary"]+"**"+"\n"+"Temparature : " +"**"+ str(result["currently"]["temperature"])+"**" +'\n'
							+"Apparent Temparature : "+"**"+str(result["currently"]["apparentTemperature"])+"**"+"\n"+"Dew Point : "+"**"+str(result["currently"]["dewPoint"])+"**"+"\n"+"Humidity : "+"**"+str(result["currently"]["humidity"])+"**"  
				})
			if content[1] == "giphy":
				text = content[2:]
				text = " ".join(text)
				im = str(self.g.search(text))
				message = im[:im.find("?")]
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": message
					})
			if content[1] == "pnr":
				message = self.pnr.get_pnr(content[2])
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": message
					})
			if content[1] == "mustread":
				email = self.mustread.get_email(self.client.get_members(),msg["content"])
				senderusername = self.mustread.get_username(self.client.get_members(),msg["sender_email"])
				print(email)
				self.client.send_message({
					"type": "private",
					"to": email,
					"content": "**"+senderusername+"** mentioned you in must read ! \nThe message says : "+" ".join(content[2:])
					})
			if content[1] == "poll":
				if content[2] == "create":
					print(",".join(content[4:]))
					idno = self.poll.create_poll(content[3],content[4:])
					self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": "Poll Successfully Created and id is : **"+str(idno)+"**"
					})
				elif content[2] == "show":
					if content[3]=="all":
						polldetails = self.poll.show_allpoll()
						self.client.send_message({
						"type": "stream",
						"subject": msg["subject"],
						"to": msg["display_recipient"],
						"content": polldetails
						})
					else:
						polldetails = self.poll.show_poll(content[3])
						self.client.send_message({
						"type": "stream",
						"subject": msg["subject"],
						"to": msg["display_recipient"],
						"content": "Poll ID: **"+polldetails["id"]+"**\n Question : **"+polldetails["pollname"]+"**\nOption : **"+polldetails["options"]+"**\n Votes : **"+polldetails["votes"]+"**"
						})
				elif content[2] == "vote":
					vote = self.poll.vote_poll(content[3],content[4])
					self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": "Your Vote Has Been Recorded!"
					})
				elif content[2] == "delete":
					if content[3] == "all":
						deleted = self.poll.delete_allpoll()
						self.client.send_message({
						"type": "stream",
						"subject": msg["subject"],
						"to": msg["display_recipient"],
						"content": "all polls has been removed from database"
						})
					else:
						deleted = self.poll.delete_poll(content[3])
						self.client.send_message({
						"type": "stream",
						"subject": msg["subject"],
						"to": msg["display_recipient"],
						"content": "The given poll has been removed from database"
						})
			if content[1] == 'motivate':
				quote_data = self.motivate.get_quote()
				self.client.send_message({
					"type": "stream",
					"to": stream_name,
					"subject": stream_topic,
					"content": quote_data
					})
			if content[1] == "shortenurl":
				short_url = self.shortenedurl.get_shorturl(content)
				self.client.send_message({
					"type": "stream",
					"to": stream_name,
					"subject": stream_topic,
					"content": short_url
					})
			if content[1] == 'hackernews' or content[1] == 'hn' or content[1] == 'HN':
				news = self.hacknews.get_hackernews()
				self.client.send_message({
					"type": "stream",
					"to": stream_name,
					"subject": stream_topic,
					"content": news
					})
			if content[1] == "twitter":
				#tweets = self.tw.get()
				#print(tweets)
				if len(content) > 2 and content[2] == "post":
					if self.tw.stream == msg["display_recipient"]:
						status = self.tw.post(" ".join(content[3:]))
						x = json.dumps(status._json)
						x = json.loads(x)
						message = "https://twitter.com/{}/status/{}".format(x["user"]["screen_name"], x["id_str"])
						message = "Tweet Posted\n" + message
						self.client.send_message({
							"type": "stream",
							"subject": msg["subject"],
							"to": msg["display_recipient"],
							"content": message
							}) 
					else:
						message = "Use the stream **{}** to post a tweet".format(self.tw.stream)
						self.client.send_message({
							"type": "private",
							"to": sender_email,
							"content": message
							})
				if len(content) > 2 and content[2] == "post_image":
					if self.tw.stream == msg["display_recipient"]:
						status = self.tw.post_image(content[3], " ".join(content[4:]))
						if isinstance(status, str):
							message = status
						else:
							x = json.dumps(status._json)
							x = json.loads(x)
							message = "https://twitter.com/{}/status/{}".format(x["user"]["screen_name"], x["id_str"])
							message = "Tweet Posted\n" + message
						self.client.send_message({
							"type": "stream",
							"subject": msg["subject"],
							"to": msg["display_recipient"],
							"content": message
							}) 
					else:
						message = "Use the stream **{}** to post a tweet".format(self.tw.stream)
						self.client.send_message({
							"type": "private",
							"to": sender_email,
							"content": message
							})
			if content[1] not in self.subkeys:
				ip = content[1:]
				ip = " ".join(ip)
				message = self.chatbot.get_response(ip).text
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": message
					})
		if self.urls(" ".join(content)):
			summary = self.w.wiki(" ".join(content))
			if summary:
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": summary
					})
		elif "omega" in content and content[0] != "omega":
			self.client.send_message({
				"type": "stream",
				"subject": msg["subject"],
				"to": msg["display_recipient"],
				"content": "Alas! Finally you called me :blush:"
				})
		else:
			return

def main():
	bot = ZulipBot()
	bot.client.call_on_each_message(bot.process)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Thanks for using Omega Bot. Bye!")
		sys.exit(0)