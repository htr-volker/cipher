import functions, animations

def main():
    animations.type_animation('Enter filename: ', 0.05)
    filename = input()
    encode_file(filename)
    print(f'{filename} encoded and saved to {filename}_encoded')
    

def encode_file(filename):
    with open(filename, "r") as file:
        contents = file.readlines()

    with open(f"{filename}_encoded", "w") as file:
        for line in contents:
            file.write(functions.encode(line) + '\n')

if __name__ == "__main__": main()