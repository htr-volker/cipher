import cipher

def main():
    cipher.type_animation('Enter phrase: ', 0.05)
    phrase = input()
    print(f'Output: {cipher.encode(phrase)}')

if __name__ == "__main__": main()