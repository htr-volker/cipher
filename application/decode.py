import functions, animations
import os

def main():
    # Loading
    os.system('clear')
    # print('\n')
    print(animations.divider)
    print(animations.title)
    animations.technobabble()
    print()
    animations.sleep(1)
    print(animations.divider, '\n', end='')
    animations.sleep(3)

    # User Input
    animations.type_animation(f'{animations.Style.RESET_ALL}{animations.Fore.GREEN}Enter filename: {animations.Style.RESET_ALL}', 0.05)
    filename = input()
    print()
    animations.sleep(3)

    # Decode
    decode_file(filename)
    
    # Close
    animations.type_animation(f'{animations.Style.BRIGHT}{animations.Fore.GREEN}Decoding Successful.', 0.05)
    animations.sleep(0.5)
    print('\n')
    animations.type_animation(f'{animations.Style.BRIGHT}{animations.Fore.GREEN}Logging off.', 0.05)
    print('\n')
    print(animations.divider)
    animations.sleep(3)
    print()


def decode_file(filename):
    print(f'{animations.Style.RESET_ALL}{animations.Fore.GREEN}{animations.decode_border(fill="-")}')
    animations.sleep(0.1)
    print(f'{animations.Style.RESET_ALL}{animations.Fore.GREEN}{animations.decode_border(message=f"{animations.Fore.YELLOW}Initialising . . .{animations.Fore.GREEN}", fill="-")}')
    animations.sleep(0.1)
    print(f'{animations.Style.RESET_ALL}{animations.Fore.GREEN}{animations.decode_border(fill="-")}')
    animations.sleep(1)
    print(f'{animations.Style.RESET_ALL}{animations.Fore.GREEN}{animations.decode_border(message=f"{animations.Fore.YELLOW}START OF FILE{animations.Fore.GREEN}", fill="-")}')
    print(f'{animations.Style.RESET_ALL}{animations.Fore.GREEN}{animations.decode_border()}')
    animations.sleep(1)

    with open(filename, "r") as file:
        contents = file.readlines()

    output = []
    for line in contents:
        line = functions.decode(line[:-1])
        animations.decode_animation(line[:-1], 0.05)
        output.append(line)
    
    animations.sleep(1)
    print(f'{animations.Style.RESET_ALL}{animations.Fore.GREEN}{animations.decode_border()}')
    print(f'{animations.Style.RESET_ALL}{animations.Fore.GREEN}{animations.decode_border(message=f"{animations.Fore.YELLOW}END OF FILE{animations.Fore.GREEN}",fill="-")}')
    print(f'{animations.Style.RESET_ALL}{animations.Fore.GREEN}{animations.decode_border(fill="-")}')
    print()

    if input(f"{animations.Style.RESET_ALL}{animations.Fore.GREEN}Save contents to file? [Y/n] ").lower() in ["y", ""]:
        with open(f"{filename}_decoded", "w") as file:
            for line in output:
                file.write(line)
        animations.sleep(1)
        print()
        animations.type_animation(f"{animations.Fore.GREEN}Output saved to {animations.Style.RESET_ALL}{filename}_decoded", 0.05)
        print()
    
    animations.sleep(1)
    print()
    animations.sleep(1)

if __name__ == "__main__": main()