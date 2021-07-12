from time import sleep
import random
from string import ascii_letters
from colorama import Fore, Style
import os

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
        "targetting"
    ],
    "adjectives" : [
        "crypto",
        "efficient",
        "global",
        "local"
    ],
    "nouns" : [
        "portal",
        "decrypter",
        "encrypter",
        "mind-palace",
        "808s",
        "AI",
        "compressor",
        "compression",
        "variable"
    ]
}

def encode(string):
    output = ''
    for character in string:
        character_unicode = ord(character)
        if character_unicode <= 65:
            divisor = 9
        else:
            divisor = random.randint(1,8)
        output += chr(character_unicode * divisor)
        output += str(divisor)
    return output

def decode(string):
    output = ''
    console = ''
    string = string.replace(' ', '')
    for character in f'{Style.RESET_ALL}{Fore.GREEN}-{{{{ {Fore.YELLOW}Initialising... {Fore.GREEN}}}}}-':
        console += character
        print(f'\r{console}', end='', flush=True)
        sleep(0.05)
    sleep(1)
    print('\r                                 ', end='', flush=True)
    for i in range(0,len(string),2):
        character_unicode = ord(string[i])
        divisor = string[i+1]
        if i != len(string)-2:
            for i in range(0,random.randint(25,200)):
                print(f'\r{Style.RESET_ALL}{Fore.GREEN}-{{{{ {Fore.LIGHTGREEN_EX}{output}' f'{Fore.YELLOW}{random.choice(ascii_letters)}{Fore.GREEN} }}}}-', end='', flush=True)
                sleep(0.01)
        output += chr(int(character_unicode / int(divisor)))
    print(f'\r{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}-{{{{ {Fore.LIGHTGREEN_EX}{output}{Fore.GREEN} }}}}- ', flush=True)
    return output

def lowest_factor(number):
    for i in range(2,number+1):
        if number % i == 0:
            return i

def type_animation(string, speed):
    output = ''
    for character in string:
        output += character
        print(f'\r{output}', end='', flush=True)
        sleep(speed)

def technobabble():
    print(f'{Fore.GREEN}{Style.BRIGHT}Loading . . .')
    for _ in range(random.randint(7,10)):
        output = f"{Fore.RED}{random.choice(technobabble_words['verbs'])} {random.choice(technobabble_words['adjectives'])} {random.choice(technobabble_words['nouns'])} . . ."
        type_animation(output, 0.02)
        print()
