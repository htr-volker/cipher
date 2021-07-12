import cipher

def main():
    print(cipher.title)
    cipher.type_animation(f'{cipher.Style.RESET_ALL}{cipher.Fore.GREEN}Enter characters: {cipher.Style.RESET_ALL}', 0.05)
    word = input()
    print()
    decoded = cipher.decode(word)
    print()
    cipher.sleep(1)
    cipher.type_animation(f'{cipher.Style.BRIGHT}{cipher.Fore.GREEN}Decoding Successful. {cipher.Style.NORMAL}The message is: {cipher.Style.BRIGHT}{decoded}', 0.05)
    print()
    cipher.sleep(1)

if __name__ == "__main__": main()