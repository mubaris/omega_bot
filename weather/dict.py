import requests
import pprint
p = pprint.PrettyPrinter()
''' class Dictonary(): '''
def words(word):
    url  = 'https://wordsapiv1.p.mashape.com/words/'+word 
    r=requests.get(url)
    results=r.json()
    return results


res=words('hello')

p.pprint(res)
''' for i in range(len(res["results"])-1):
    p.pprint(res["results"][i])  '''      

