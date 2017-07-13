from slackclient import SlackClient
import os
import pprint

def getID(userList,name,pp):
    for member in userList["members"]:
        if member["name"] == name:
            # print("{} {}".format(member["name"],member["id"]))
            pp.pprint(member)

pp = pprint.PrettyPrinter(indent=4)

token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" 
sc = SlackClient(token)

# channel_list = sc.api_call(
#         "channels.list",
#         exclude_archived=1
#         )
userList = sc.api_call(
        "users.list",
        exclude_archived=1
        )

# getID(userList,"hagiwara",pp)
getID(userList,"ito",pp)
# getID(userList,"yamamoto",pp)

# pp.pprint(userList)

# for member in userList["members"]:
#     if member["name"] == "ito":
#         print("{} {}".format(member["name"],member["id"]))


# for channel in channel_list["channels"]:
#     print("name = {:10} , id = {:10}".format(channel["name"],channel["id"]))
#     if channel["name"] == "bot_dev":
#         bot_dev_c = channel

# channel_info = sc.api_call(
#         "channels.info",
#         channel=bot_dev_c["id"]
# )
# pp.pprint(channel_info)
# pp.pprint(channel_list["channels"])
# print(channel_info)
