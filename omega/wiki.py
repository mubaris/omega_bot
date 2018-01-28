import wikipedia
from nltk import sent_tokenize
import re

class WikiPedia(object):
	def __init__(self):
		self.w = wikipedia
	def urls(self, link):
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', link)
		return urls
	def wiki(self, link):
		urls = self.urls(link)
		for url in urls:
			if "en.wikipedia.org/wiki/" in url:
				title = url.split("en.wikipedia.org/wiki/")[1]
				summary = self.w.summary(title, sentences=4)
				summary_list = sent_tokenize(summary)
				summary = "\n".join(summary_list)
				summary = "**WikiPedia Summary**\n```\n" + summary + "\n```" 
				return summary