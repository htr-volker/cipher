#!/bin/bash
sudo apt install python3 python3-venv python3-pip

python3 -m venv venv
source venv/bin/activate

pip3 install -U pip
pip3 install -r requirements.txt
