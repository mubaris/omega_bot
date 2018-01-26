# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json

# TODO: replace with your own app_id and app_key
app_id = '023c95f9'
app_key = 'ce3926d60a79be01b44805b4e9d53288'

language = 'en'
word_id = 'Ace'

''' url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key}) '''

''' print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json())) '''

''' res = r.json() '''

''' print("\n")
print("\n")
print("\n") '''
''' for i in range(len(res["results"][0]["lexicalEntries"][0]["entries"][0]["senses"])-1):
    print(res["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][i]["definitions"][0]) '''


class Dictionary():
    def words(self,word):
        url= 'https://od-api.oxforddictionaries.com:443/api/v1/entries/en/' + word.lower()
        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        res=r.json()
        print(res)
        print('\n')
        print('\n')
        print('\n')
        print(res["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0])
        result=''
        for i in range(len(res["results"][0]["lexicalEntries"][0]["entries"][0]["senses"])):
           result=result+str(i+1)+'.'+res["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][i]["definitions"][0]+'\n'
        return result   

        