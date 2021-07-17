#!/bin/bash
sudo apt install python3 python3-pip

python3 -m pip install -U pip
python3 -m pip install -r requirements.txt

sudo rm -rf /opt/cipher || true
sudo cp -r . /opt/cipher

sudo chmod a+x cipher-encode
sudo chmod a+x cipher-decode

sudo rm -f /bin/cipher-encode || true
sudo rm -f /bin/cipher-decode || true

sudo cp cipher-encode /bin/cipher-encode
sudo cp cipher-decode /bin/cipher-decode
