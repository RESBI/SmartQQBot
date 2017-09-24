# coding: utf-8
from random import randint
import requests

from smart_qq_bot.signals import on_all_message

url = 'http://www.tuling123.com/openapi/api'
apikey = '6c2cfaf7a7f088e843b550b0c5b89c26'

@on_all_message
def turing_robot(msg, bot):
    TEMP_PATH = "/var/smbfile/usb/USB1/PythonGits/bot/smart_qq_plugins/turing-exs/"
    group_code = str(msg.group_code)
    group_id = str(bot.get_group_info(group_code=group_code).get('id'))
    """
    :type bot: smart_qq_bot.bot.QQBot
    :type msg: smart_qq_bot.messages.QMessage
    """
    querystring = {
        "key": apikey,
        "info": msg.content,
    }
    response = requests.request("GET", url, params=querystring)

    if "ShutUp" in msg.content:
        bot.reply_msg(msg, "Bot : " + "Okey Okey..I shutup.")
        f = open(TEMP_PATH + str(group_id) + ".txt" ,"w+")
        f.write("1")
        f.close()

    if "TalkSomething" in msg.content:
        bot.reply_msg(msg, "Bot : " + "So...")
        f = open(TEMP_PATH + str(group_id) + ".txt" ,"w+")
        f.write("0")
        f.close()

    try:
        a = open(TEMP_PATH + str(group_id) + ".txt" ,"r")
        b = a.read()
        a.close()
    except:
        f = open(TEMP_PATH + str(group_id) + ".txt" ,"w+")
        f.write("0")
        f.close()
        a = open(TEMP_PATH + str(group_id) + ".txt" ,"r")
        b = a.read()
        a.close()

    if "0" in b:
        if "Bot : " in msg.content:
            print("",end = "\r")
        else:
            response_json = response.json()
            temps = response_json.get('text')
            bot.reply_msg(msg, "Bot : " + temps)
