from googletrans import Translator

class Translate(object):
	def __init__(self):
		self.trans = Translator()
	def translate(self, text):
		ttext = self.trans.translate(text).text
		pron = self.trans.translate(text).pronunciation
		if pron == None:
			pron = ttext
		message = "**" + ttext + "**"
		message += "(" + pron + ")"
		return message