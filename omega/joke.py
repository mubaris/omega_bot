import pprint
import requests

class Joke():
    def tellJoke(self):
        joke=requests.get('https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke').json()
        print(joke["setup"])
        print(joke["punchline"])
        result='**'+joke["setup"]+'**'+'\n'+'Answer : '+ joke["punchline"]
        return result