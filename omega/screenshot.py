import requests
import urllib
import webbrowser
from urllib.parse import urlencode
from urllib.request import urlretrieve

class Ss(object):
    def __init__(self):
        self.ids = {}
    def get_ss(self, url):
        try:
            params = urlencode({"url": url, "access_key": "3ac7b2dbeb524996bae388718eb31ede"})
            message=urlretrieve("https://apileap.com/api/screenshot/v1/urltoimage?" + params, "screenshot.jpeg")
            webbrowser.open("https://apileap.com/api/screenshot/v1/urltoimage?" + params)
            return "https://apileap.com/api/screenshot/v1/urltoimage?" + params
        except KeyError:
            message = "Enter a valid PNR number"
        return message