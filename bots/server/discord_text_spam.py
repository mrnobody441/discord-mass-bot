#
# @author Pukoa
# @created Fri Jan 04 2019 00:58:07 GMT-0500 (Eastern Standard Time)
# @copyright 2018 - 2022
# @license CC BY-NC-ND 3.0 US | https://creativecommons.org/licenses/by-nc-nd/3.0/us/
# @last-modified Tue Mar 05 2019 02:11:47 GMT-0500 (Eastern Standard Time)

import discum
import time
import sys
import random
import os
import subprocess
import socket
sys.path.append("./.")
from config import *

token = sys.argv[1]
global spam_text
spam_text = sys.argv[2]
global bot # Declaring discum global
if(os.path.exists("proxies.txt")):
    pnp = sys.argv[3].split(':')
if ':' in token: # Email and pass check (Seeing if there is a basic combo list)
    enp = token.split(':')
    email = enp[0]
    password = enp[1]
    if autojoinServer == True:
        if sys.platform == "win32":
            p = subprocess.Popen(['python','bots/misc/joinServer.py',email,password,inviteLink,useBrowser],shell=True)
            p.wait()
        else:
            p = subprocess.Popen(['python','bots\misc\joinServer.py',email,password,inviteLink,useBrowser],shell=False)
            p.wait()
    if(os.path.exists("proxies.txt")): # Checking root folder for proxies
        bot = discum.Client(email=email,password=password, token="none", proxy_host=pnp[0], proxy_port=pnp[1], log=discumLog)
    else:
        bot = discum.Client(email=email,password=password, token="none",log=discumLog)
else:
    if autojoinServer == True:
        if sys.platform == "win32":
            p = subprocess.Popen([pythonCommand,'bots\misc\joinServer2.0.py',token,inviteLink,sys.argv[3]],shell=True)
            p.wait()
        else:
            p = subprocess.Popen([pythonCommand,'bots\misc\joinServer2.0.py',token,inviteLink,sys.argv[3]],shell=False)
            p.wait()
    if(os.path.exists("proxies.txt")):
        bot = discum.Client(token=token, proxy_host=pnp[0], proxy_port=pnp[1], log=discumLog)
    else:
        bot = discum.Client(token=token,log=discumLog)

while True:
    spam_text = sys.argv[2]
    print("Started Text Spam")
    if os.path.exists('text.txt'): # opening our spam text file
        if textRandom == False and textFull == False:
            lines = open('text.txt').read().splitlines()
            spam_text = lines[0]
        elif textFull == True:
            with open('text.txt', 'r', encoding='utf-8') as spamtextfile:
                spam_text = spamtextfile.read()
        else:
            lines = open('text.txt').read().splitlines()
            spam_text = random.choice(lines)
    bot.sendMessage(DiscordChannel,spam_text) # Send Message
    time.sleep(SpamSpeed) #Wait seconds
