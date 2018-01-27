import json
import requests

class Poll(object):
    def __init__(self):
        self.ids = {}
    def show_poll(self,idno):
        try:
            data = json.load(open('poll.json'))
            for i in range(0,data["polls"].__len__()):
                if data["polls"][i]["id"]==idno:
                    return data["polls"][i]
            return KeyError
        except KeyError:
            message = "Invalid ID"
        return message
    
    def show_allpoll(self):
        try:
            data = json.load(open('poll.json'))
            message=""
            for i in range(0,data["polls"].__len__()):
               message+="Poll ID: **"+data["polls"][i]["id"]+"**\n Question : **"+data["polls"][i]["pollname"]+"**\nOption : **"+data["polls"][i]["options"]+"**\n Votes : **"+data["polls"][i]["votes"]+"**\n\n\n"
            return message
        except KeyError:
            message = "Something went wrong"
        return message
    def vote_poll(self,idno,selectedoption):
        try:
            data = json.load(open('poll.json'))
            for i in range(0,data["polls"].__len__()):
                if data["polls"][i]["id"]==idno:
                    tovote=data["polls"][i]["options"].split()
                    votecount=data["polls"][i]["votes"].split(",")
                    for p in range(0,tovote.__len__()):
                        if selectedoption==tovote[p]:
                            print(votecount[p])
                            votecount[p] = str(int(votecount[p])+1)
                            print(votecount[p])
                    data["polls"][i]["votes"]=""
                    for p in range(0,tovote.__len__()):
                        if p==tovote.__len__()-1:
                            data["polls"][i]["votes"]+=votecount[p]
                        else:
                            data["polls"][i]["votes"]+=votecount[p]+","
                    with open('poll.json', mode='w', encoding='utf-8') as f:
                        json.dump(data, f)
                    return "Succesfully Voted"
            return KeyError
        except KeyError:
            message = "Invalid ID"
        return message

    def delete_poll(self,idno):
        try:
            data = json.load(open('poll.json'))
            for i in range(0,data["polls"].__len__()):
                if data["polls"][i]["id"]==idno:
                    del data["polls"][i]
                    with open('poll.json', mode='w', encoding='utf-8') as f:
                        json.dump(data, f)
                    return "Deleted"
            return KeyError
        except KeyError:
            message = "Invalid ID"
        return message

    def delete_allpoll(self):
        try:
            data = json.load(open('poll.json'))
            for i in range(data["polls"].__len__()-1,-1,-1):
                del data["polls"][i]
            with open('poll.json', mode='w', encoding='utf-8') as f:
                json.dump(data, f)
            return "Deleted"
            return KeyError
        except KeyError:
            message = "Something went wrong"
        return message

    def create_poll(self,count,content):
        try:
            options = content[1:]
            l = list(content)
            print("this one")
            print(l)
            startquestion=-1
            end=-1
            endquestion=-1
            for j in range(0,l.__len__()):
                if l[j]=="question":
                    startquestion=j+1
                elif l[j]=="option":
                    endquestion=j
                    end=j+1
           
            question = " ".join(l[startquestion:endquestion])
            options = " ".join(l[end:])
            data = json.load(open('poll.json'))
            votes = []
            idno = int(data["polls"][data["polls"].__len__()-1]["id"])+1
            for i in range(0,int(count)):
                votes.append("0")
            data["polls"].append({
                "id":str(idno),
                "pollname":question,
                "options":options,
                "votes" : ",".join(votes)
            })
            with open('poll.json', mode='w', encoding='utf-8') as f:
                json.dump(data, f)
            return int(data["polls"][data["polls"].__len__()-1]["id"])
        except KeyError:
            message = "Some Error Occured"
        return message