import random
import os

def encode(string):
    output = ''
    for character in string:
        character_unicode = ord(character)
        if character_unicode <= 65:
            multiple = 9
        else:
            multiple = random.randint(1,8)
        output += chr(character_unicode * multiple)
        output += str(multiple)
    return output

def decode(string):
    output = ''
    string = string.replace(' ', '')
    for i in range(0,len(string),2):
        character_unicode = ord(string[i])
        divisor = string[i+1]
        output += chr(int(character_unicode / int(divisor)))
    return output

# def decode(string):
#     output = ''
#     console = ''
#     string = string.replace(' ', '')
#     for character in f'{Style.RESET_ALL}{Fore.GREEN}-{{{{ {Fore.YELLOW}Initialising... {Fore.GREEN}}}}}-':
#         console += character
#         print(f'\r{console}', end='', flush=True)
#         sleep(0.05)
#     sleep(1)
#     print('\r                                 ', end='', flush=True)
#     for i in range(0,len(string),2):
#         character_unicode = ord(string[i])
#         divisor = string[i+1]
#         if i != len(string)-2:
#             for i in range(0,random.randint(25,75)):
#                 print(f'\r{Style.RESET_ALL}{Fore.GREEN}-{{{{ {Fore.LIGHTGREEN_EX}{output}' f'{Fore.YELLOW}{random.choice(ascii_letters)}{Fore.GREEN} }}}}-', end='', flush=True)
#                 sleep(0.01)
#         output += chr(int(character_unicode / int(divisor)))
#     print(f'\r{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}-{{{{ {Fore.LIGHTGREEN_EX}{output}{Fore.GREEN} }}}}-', flush=True)
#     return output


