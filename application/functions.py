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
