import requests

class Mustread(object):
	def __init__(self):
		self.ids = {}
		#json = requests.get("https://api.coinmarketcap.com/v1/ticker/").json()
		#for cr in json:
			#self.ids[cr["symbol"]] = cr["id"]

	def get_email(self, users, username):
		try:
			json = users
			start=-1
			end=-1
			l = list(username)
			for j in range(0,l.__len__()):
				if l[j]=="*" and l[j+1]=="*" and start==-1:
					start=j+2
				elif l[j]=="*" and l[j+1]=="*" and start!=-1:
					end=j
			newusername="".join(l[start:end])
			for i in range(0,json["members"].__len__()):
				if json["members"][i]["full_name"]==newusername:
					return json["members"][i]["email"]
			return "iit2016106@iiita.ac.in"
		except KeyError:
			message = "Could not find an email address"
		return message

	def get_username(self, users, emailid):
		try:
			json = users
			for i in range(0,json["members"].__len__()):
				if json["members"][i]["email"]==emailid:
					return json["members"][i]["full_name"]
			return "iit2016106@iiita.ac.in"
		except KeyError:
			message = "Could not find an email address"
		return message