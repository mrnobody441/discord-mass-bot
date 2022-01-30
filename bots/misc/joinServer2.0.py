#
# @author Pukoa
# @created Fri Jan 04 2019 00:58:07 GMT-0500 (Eastern Standard Time)
# @copyright 2018 - 2022
# @license CC BY-NC-ND 3.0 US | https://creativecommons.org/licenses/by-nc-nd/3.0/us/
# @last-modified Tue Mar 05 2019 02:11:47 GMT-0500 (Eastern Standard Time)

import requests
import json
import sys
import os
TOKEN = sys.argv[1]
INVITE_LINK = sys.argv[2]
PROXY = { 'http' : sys.argv[3] } 
url = 'https://discordapp.com/api/v6/invite/'+INVITE_LINK+'?with_counts=true'
print(url)
headers = {"content-type": "application/json", "Authorization": TOKEN }

r = requests.post(url,headers=headers, proxies=PROXY)
if r.status_code == 200:
    print("Token:"+"'"+TOKEN[-25]+"'"+" Joined the server")
else:
    print('error, something went wrong.')
    print('Make sure your token is correct | https://discordhelp.net/discord-token')
    print(r.json())