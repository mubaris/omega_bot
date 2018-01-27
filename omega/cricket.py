import requests

class Cricket():
    def news(self):
        r = requests.get('https://newsapi.org/v2/everything?sources=espn-cric-info&apiKey=c4df6c22455b4179861eb40cd6e02aba').json()
        result=''
        for i in range(10):
            result = result +str((i+1))+'.'+'['+r["articles"][i]["title"]+']'+'('+r["articles"][i]["url"]+')'+'\n' + '\n'
        print(result)
        return result
        

