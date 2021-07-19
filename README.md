# Cipher

***Cipher v0.0.1*** is an entirely legitimate, highly sophisticated, top-of-the-line encoding/decoding program that can crack even the toughest of encryptions!

<details>
<summary>Disclaimer</summary>
"Cipher" is neither sophisticated or top-of-the-line! It's a silly little Python program I've written that can 'encode' the contents of files with a very simple, easily crackable algorithm, and then 'decode' it in kind.

The majority of the effort for this program went into creating the animations to give the feeling of a hefty, sophisticated hacking program that gives you that classic Matrix-esque "I'm IN" moment.
</details>

## Installation on Ubuntu

Installation of ***Cipher*** is simple. First, clone down this repository to your machine with:

```bash
git clone https://github.com/htr-volker/cipher
```

Then run the 'install.sh' script on your bash terminal:

```bash
./install.sh
```

<details>
<summary>More info</summary>

The install script will copy the contents of this repository into `/opt/cipher` and copy two scripts (`cipher-encode` and `cipher-decode`) into `/bin` to make the app executable from anywhere in the file system.

</details>

## Decoding a File

To run ***Cipher***'s decode functionality, start the program with the command:

```bash
cipher-decode
```

You'll see a screen that looks like this:

```text
===========================================================================================

  e88'Y88 ,e,          888                              e88 88e         e88 88e         d88 
 d888  'Y  "  888 88e  888 ee   ,e e,  888,8,          d888 888b       d888 888b       d888 
C8888     888 888 888b 888 88b d88 88b 888 "    888   C8888 8888D     C8888 8888D     d"888 
 Y888  ,d 888 888 888P 888 888 888   , 888             Y888 888P  d8b  Y888 888P  d8b   888 
  "88,d88 888 888 88"  888 888  "YeeP" 888              "88 88"   Y8P   "88 88"   Y8P   888 
              888                                                                           
              888                                                                           

Loading . . .
extending light portal . . .                    5.6MB   ✓
opening public encryptors . . .                 8.0MB   ✓
unzipping stealthy web . . .                    7.5MB   ✓
encrypting private webs . . .                   4.7MB   ✓
playing efficient decryptor . . .               5.8MB   ✓
playing private 808s . . .                      3.2MB   ✓
flushing emphatic web . . .                     6.2MB   ✓

===========================================================================================
Enter filename:
```

Simply type in the filename of the file you want to decode, and watch the magic happen!

> Note: You can use the `sample_secret_message.txt` file provided with this repo to test the decoding program.

Once the decoding has finished, you will be asked whether you'd like to save the decoded output to a file.

Either `y`, `Y` or just hitting the `Enter` key will save the output to a file with the name `<original_filename>_decoded`. Any other input will skip this stage.

### Issues

There are a couple of known issues with the program:
- Entering a filename that doesn't exist will result in an error and the program exiting prematurely. If this occurs, just run the program again and be sure to enter the right filename! In the future I plan to implement some error-handling to prevent this from breaking the app.
- Attempting to decode a file that is not encoded will result in an error and exit the program prematurely. Again, I plan to implement some error-handling to handle this issue.
- Resizing the window will result in the terminal formatting messing up. It will functionally still work, but you'll see some strange visual artifacts. Don't panic!

## Encoding a File

If you'd like to encode a file, simply run:

```bash
cipher-encode
```

A much simpler UI will appear on your terminal prompting you to provide the filename whose contents you'd like to encode.

It will then create a new file with the encoded output with the name `<original_filename>_encoded`.

Files encoded with `cipher-encode` can then be decoded with `cipher-decode`.
