import pprint
import zulip
import requests
from geocode import Geocode
from weather import Weather 
from dict import Dictionary
from joke import Joke
p = pprint.PrettyPrinter()
BOT_MAIL = "awesome-bot@chunkzz.zulipchat.com"
geo = Geocode()
weather  = Weather()
dict = Dictionary()
joke = Joke()
class ZulipBot(object):
	def __init__(self):
		self.client = zulip.Client(site="https://chunkzz.zulipchat.com/api/")
		self.subscribe_all()
		#self.crypto = Crypto()

	def subscribe_all(self):
		json = self.client.get_streams()["streams"]
		streams = [{"name": stream["name"]} for stream in json]
		self.client.add_subscriptions(streams)

	def process(self, msg):
		content = msg["content"].split()
		sender_email = msg["sender_email"]
		ttype = msg["type"]
		name = msg["sender_full_name"]
		p.pprint(msg)
		print(content)

		if sender_email == BOT_MAIL:
			return 

		print("yeah")

		if content[0] == "omega" and content[1] == "weather" :
			# Write code here
			place = content[2]
			result = weather.getWeather(geo.convert(place))			
			self.client.send_message({
				"type": "stream",
				"subject": msg["subject"],
				"to": msg["display_recipient"],
				"content": "**"+"Weather update of "+place+"**"+"\n"+"Summary : " + "**"+result["currently"]["summary"]+"**"+"\n"+"Temparature : " +"**"+ str(result["currently"]["temperature"])+"**" +'\n'
				+"Apparent Temparature : "+"**"+str(result["currently"]["apparentTemperature"])+"**"+"\n"+"Dew Point : "+"**"+str(result["currently"]["dewPoint"])+"**"+"\n"+"Humidity : "+"**"+str(result["currently"]["humidity"])+"**"  
				})
		elif content[1] == "define" and content[0] == "omega" :
			word = content[2]
			result=dict.words(word)
			print(result)
			self.client.send_message({
				"type": "stream",
				"subject": msg["subject"],
				"to": msg["display_recipient"],
				"content": "**"+word+" means :"+"**"+'\n'+result  
				})
		elif content[1] == "tell" and content[2] == "a" and content[3] == "joke" and content[0] == "omega" :
			text=joke.tellJoke()
			self.client.send_message({
				"type": "stream",
				"subject": msg["subject"],
				"to": msg["display_recipient"],
				"content": text  
				})		
		else:
			return

def main():
	bot = ZulipBot()
	bot.client.call_on_each_message(bot.process)

if __name__ == "__main__":
	main()