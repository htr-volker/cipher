from colorama import Fore, Style
from time import sleep
from string import ascii_letters
import random
import os
import re

title = f'''{Fore.GREEN}{Style.BRIGHT}
  e88'Y88 ,e,          888                              e88 88e         e88 88e         d88 
 d888  'Y  "  888 88e  888 ee   ,e e,  888,8,          d888 888b       d888 888b       d888 
C8888     888 888 888b 888 88b d88 88b 888 "    888   C8888 8888D     C8888 8888D     d"888 
 Y888  ,d 888 888 888P 888 888 888   , 888             Y888 888P  d8b  Y888 888P  d8b   888 
  "88,d88 888 888 88"  888 888  "YeeP" 888              "88 88"   Y8P   "88 88"   Y8P   888 
              888                                                                           
              888                                                                           
'''

divider = f'{Fore.GREEN}{Style.BRIGHT}' + ('=' * os.get_terminal_size().columns)

initialising = f'''
ooooo              o8o      .    o8o            oooo   o8o            o8o                                          
`888'              `"'    .o8    `"'            `888   `"'            `"'                                          
 888  ooo. .oo.   oooo  .o888oo oooo   .oooo.    888  oooo   .oooo.o oooo  ooo. .oo.    .oooooooo                  
 888  `888P"Y88b  `888    888   `888  `P  )88b   888  `888  d88(  "8 `888  `888P"Y88b  888' `88b                   
 888   888   888   888    888    888   .oP"888   888   888  `"Y88b.   888   888   888  888   888                   
 888   888   888   888    888 .  888  d8(  888   888   888  o.  )88b  888   888   888  `88bod8P'  .o. .o. .o.      
o888o o888o o888o o888o   "888" o888o `Y888""8o o888o o888o 8""888P' o888o o888o o888o `8oooooo.  Y8P Y8P Y8P      
                                                                                       d"     YD                   
                                                                                       "Y88888P'                                                                                                                  
'''

technobabble_words = {
    "verbs" : [
        "flushing",
        "extending",
        "energising",
        "initialising",
        "targeting",
        "resetting",
        "starting",
        "inheriting",
        "decrypting",
        "encrypting",
        "unzipping",
        "playing",
        "retrofitting",
        "launching",
        "closing",
        "establishing"
    ],
    "adjectives" : [
        "crypto",
        "efficient",
        "global",
        "local",
        "secret",
        "sensitive",
        "emphatic",
        "empathic",
        "silent",
        "stealthy",
        "light",
        "dark",
        "inefficient",
        "private",
        "public"
    ],
    "nouns" : [
        "portal",
        "decryptor",
        "encryptor",
        "mind-palace",
        "808",
        "AI",
        "compressor",
        "compression",
        "variable",
        "password",
        "jazz",
        "web",
        "connection",
        "port",
        "VPN",
        "learner",
        "keylogger",
        "connection"
    ]
}

def type_animation(string, speed):
    output = ''
    for character in string:
        output += character
        print(f'\r{output}', end='', flush=True)
        sleep(speed)

def load_animation(number, speed):
    unit = "kB"
    for i in range(0,number,5):
        if i >= 1024:
            value = f"{(i/1000):.2}"
            unit = 'MB '
        else:
            value = i
        print('\r' + '\t'*6 + f'{Fore.LIGHTRED_EX}{Style.BRIGHT}{value}{unit}', end='', flush=True)
        sleep(speed)
    print(f'{Fore.GREEN}{Style.BRIGHT}\t✓')

def decode_animation(string, speed):
    output = ''
    for character in string:
        for _ in range(0,random.randint(3,15)):
            message = f'{Fore.LIGHTGREEN_EX}{output}{Fore.YELLOW}{random.choice(ascii_letters)}{Fore.GREEN}'
            print(f'\r{Style.RESET_ALL}{Fore.GREEN}{decode_border(message=message)}', end='', flush=True)
            sleep(speed)
        output += character
    message = f'{Fore.LIGHTCYAN_EX}{output}{Fore.GREEN} ✓'
    print(f'\r{Style.RESET_ALL}{Fore.GREEN}{decode_border(message=message)}', flush=True)
    sleep(0.5)

def decode_border(message='', fill=' '):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    if message != '':
        message += ' '
    start = '-{{ ' + message
    end = ' }}-'
    length = len(ansi_escape.sub('', start+end))
    return start + (fill * (os.get_terminal_size().columns-length)) + end
        
def technobabble():
    type_animation(f'{Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT}Loading . . .{Style.RESET_ALL}', 0.01)
    print()
    sleep(1)
    for _ in range(7):
        output = f"{Style.RESET_ALL}{Fore.RED}{random.choice(technobabble_words['verbs'])} {random.choice(technobabble_words['adjectives'])} {random.choice(technobabble_words['nouns'])}{random.choice(['s',''])} . . .{Style.RESET_ALL}"
        type_animation(output, 0.01)
        sleep(0.5)
        load_animation(random.randint(100,10000),0.00000001)