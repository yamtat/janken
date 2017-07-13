from slackclient import SlackClient
import time
import re


token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" 
sc = SlackClient(token)

def roulet(self, data):
    if "type" in data.keys():
        if data["type"] == "text":
            if re.search(u"(.*ルーレット*|.*roulet*)", data["text"]) is not None:
                return "<@" + data["user"] + "> " + u":itoretchman2:"

if sc.rtm_connect():
    while True:
        # print(sc.rtm_read())

        data = sc.rtm_read()
        # print(data)
        if len(data) > 0:
            print(data)
            for item in data:
                # print(item)
                if "type" in item.keys():
                    if item["type"] == "message":
                        # print(item)
                        sc.rtm_send_message(channel=item["channel"],message=item["text"])

        time.sleep(1)

else:
    print("Connection Failed, invalid token?")
