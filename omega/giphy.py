import giphypop
import random

class Giphy(object):
	def __init__(self):
		self.g = giphypop.Giphy(api_key="dc6zaTOxFJmzC")

	def search(self, text):
		results = [x for x in self.g.search(text)]
		im = random.choice(results)
		return im.media_url