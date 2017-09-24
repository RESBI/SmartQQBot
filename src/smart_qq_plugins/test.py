from smart_qq_bot.signals import on_all_message
import time,os
@on_all_message
def test(msg,bot):
    TEMP_PATH = "/var/smbfile/usb/USB1/PythonGits/bot/smart_qq_plugins/temppath/"
    re = ""
    """
    :type bot: smart_qq_bot.bot.QQBot
    :type msg: smart_qq_bot.messages.QMessage
    """

    if "Bot : " in msg.content:
        print("",end = "\r")
    else:
        if "Server" in msg.content:
            if "Time" in msg.content.split("Server")[1]:
                re = "Bot : Now time is:" + str(time.time())
                bot.reply_msg(msg,re)
            elif "Temp" in msg.content.split("Server")[1]:
                f = open("/sys/class/thermal/thermal_zone0/temp","r")
                re = "Bot : Now server temp is:" + str(f.read().split("\n")[0])
                f.close()
                bot.reply_msg(msg,re)
#        if "Shell" in msg.content:
#            if "cp " in msg.content or "mv " in msg.content or "wget " in msg.content or "sh " in msg.content or "curl " in msg.content or "rm " in msg.content or "dd " in msg.content:
#                re = "Bot : " + msg.content.split("Shell")[1] + " was not allowd."
#                bot.reply_msg(msg,re)
#            else:
#                os.system("%s > %stemp.txt" % (msg.content.split("Shell ")[1],TEMP_PATH))
#                a = open(TEMP_PATH + "temp.txt","r")
#                re = "Bot : \n" + a.read()
#                a.close()
#                bot.reply_msg(msg,re)