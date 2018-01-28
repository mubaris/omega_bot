import requests
import datetime

class Crypto(object):
	def __init__(self):
		self.ids = {}
		json = requests.get("https://api.coinmarketcap.com/v1/ticker/").json()
		for cr in json:
			self.ids[cr["symbol"]] = cr["id"]

	def get_price(self, symbol, curr="USD"):
		try:
			symbol = symbol.upper()
			curr = curr.upper()
			url = "https://api.coinmarketcap.com/v1/ticker/{}/?convert={}".format(self.ids[symbol], curr)
			print(url)
			json = requests.get(url).json()[0]
			if curr == "USD":
				message = "Price of **{}** is **{} {}**".format(json["name"], json["price_usd"], curr)
			else:
				curr_str = "price_" + curr.lower()
				try:
					message = "Price of **{}** is **{} {}**".format(json["name"], json[curr_str], curr)
				except KeyError:
					message = "Price of **{}** is **{} {}**".format(json["name"], json["price_usd"], "USD")
					message += "\n **{}** is a not a valid Currency".format(curr)
			message += "\n" + "Last Updated : *" + datetime.datetime.fromtimestamp(int(json["last_updated"])).strftime("%Y %B %d %H:%M:%S") + "*"
		except KeyError:
			message = "**{}** is a not a valid crypto currency".format(symbol)
		return message