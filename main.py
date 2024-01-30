import random
import time
import os
import fade
import colorama
from colorama import Fore
import webbrowser
import keyboard
import requests
webbrowser.open("discord.gg/jnn")
webbrowser.open("https://www.youtube.com/channel/UCN8LRd8JnX2FkelKfnfRRfg")

title = fade.purplepink("""
     ██╗███╗   ██╗███╗   ██╗    ██╗    ██╗██╗  ██╗███████╗
     ██║████╗  ██║████╗  ██║    ██║    ██║██║  ██║██╔════╝
     ██║██╔██╗ ██║██╔██╗ ██║    ██║ █╗ ██║███████║███████╗
██   ██║██║╚██╗██║██║╚██╗██║    ██║███╗██║██╔══██║╚════██║
╚█████╔╝██║ ╚████║██║ ╚████║    ╚███╔███╔╝██║  ██║███████║
 ╚════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝     ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝
    .gg/jnn | edi is a skid |     web     hook   spammer
""")

colorama.init(autoreset=True)
#TAKE OUT ALL OF THE COMMENTS TO SPAM MORE WEBHOOKS!

#wh2 = ""
#wh3  ""
#wh4 = ""
#wh5 = ""

print(title)
webhook = input(Fore.RED+'Enter webhook: ')
webhook_count = int(input(Fore.BLUE+"Enter how many webhook messages would you like to send?:  "))
message = input(Fore.MAGENTA+"Enter webhook message: ")
button_to_stop = input(Fore.RED+'What would you like to hold to stop webhook spam? (EG: F9): ')
cooldown = input(Fore.BLUE+"Enter Cooldown (1.5 is recommended): ")
print(f'{Fore.MAGENTA}Everything set!')
time.sleep(1)
os.system("cls")

for x in range(1,webhook_count+1):
    print(title)
    requests.post(webhook, json={'content': message})
    print(f"{Fore.RED}Sent{Fore.BLUE} Message: {Fore.MAGENTA}{message}")
    time.sleep(float(cooldown))
    os.system("cls")
    if keyboard.is_pressed(button_to_stop):
        quit()
