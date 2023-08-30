import os, json
import requests, time
from base64 import b64encode
from threading import Thread
import tls_client

os.system("cls" if os.name == "nt" else "clear")

__useragent__ = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"  #requests.get('https://discord-user-api.cf/api/v1/properties/web').json()['chrome_user_agent']
build_number = 165486  #int(requests.get('https://discord-user-api.cf/api/v1/properties/web').json()['client_build_number'])
cv = "108.0.0.0"
__properties__ = b64encode(
  json.dumps(
    {
    "os": "Windows",
    "browser": "Mozilla",
    "release_channel": "canary",
    "os_version": "10.0.22000",
    "os_arc": "x64",
    "system_locale": "en-US",
    "client_build_number": 183478,
    "nativelink_builder": 30992,
    "client_event_source": "en-US",
    "client_edvent_builder": 183478,
    "client_event_survey": "null",
    "design_id": 0
  }
,
    separators=(',', ':')).encode()).decode()


# def get_headers(token):
#   headers = {
#     "Authorization": token,
#     "Origin": "https://discord.com",
#     "Accept": "*/*",
#     "X-Discord-Locale": "en-GB",
#     "X-Super-Properties": __properties__,
#     "User-Agent": __useragent__,
#     "Referer": "https://discord.com/channels/@me",
#     "X-Debug-Options": "bugReporterEnabled",
#     "Content-Type": "application/json"
#   }
#   return headers

def get_headers(token):
  headers = {
            "Authorization":
            token,
            "accept":
            "*/*",
            "accept-language":
            "en-US",
            "connection":
            "keep-alive",
            "cookie":
            f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT":
            "1",
            "origin":
            "https://discord.com",
            "sec-fetch-dest":
            "empty",
            "sec-fetch-mode":
            "cors",
            "sec-fetch-site":
            "same-origin",
            "referer":
            "https://discord.com/channels/@me",
            "TE":
            "Trailers",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties":
            __properties__
  }
  return headers

def leave(token, guild_id):
  headers = get_headers(token)
  # headers = {"Authorization": token}
  client = tls_client.Session(client_identifier="firefox_102")
  client.headers.update(headers)
  #requests.get("https://discord.com/api/v9/users/@me", headers=headers)
  r = client.delete(f"https://canary.discord.com/api/v9/users/@me/guilds/{guild_id}", headers=headers, json={"lurking": False})
  if r.status_code in (200, 201, 204):
    print(f"Left {guild_id} successfully with {token}")
  else:
    print(f"Failed to leave {guild_id} - {r.text}")


f = open("tokens.txt", "r").readlines()
amount = int(input("[!] Amount: "))
guildx = input("[!] Guild ID: ")

left = 0 
for token in f:
  token = token.strip()
  #token = token.split(":")[2]
  if left >= amount:
    break
  left += 1
  time.sleep(0.05)
  Thread(target=leave, args=(token, guildx,)).start()