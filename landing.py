#!/usr/bin/python
import time
from time import sleep
from IPy import IP
from ios_comms import iocomms
from colorama import init, Fore, Back, Style
import sys
import os
from printslow import print_slow

timestamp = time.strftime(".%H%M%S")

__author__ = "John Ng"
__copyright__ = "Copyright 2018, John Ng"
__license__ = "MIT License"
__version__ = "v1.0 Beta"
__status__ = "Experimental"


init(strip=False)
print('\033[32;1m' + 45 *'-', ' Landing Page ' + 45 *'-')
print('This is a Python script to generate fancy commands for Cisco IOS, IOS XE, CatOS devices,')
print('A summary of what each module does will be displayed after said module is selected')
print('Each report will be generated and saved in each individual text files according to IP Address & Timestamp')
print('Please Note...Normal device config generation time and physical resources consumption still applies.')
print(Fore.CYAN + Style.BRIGHT + '\u00a9' + ' John Ng, 2018')
print(Fore.CYAN + Style.BRIGHT + '[v1.5 Beta]')
print('\033[32;1m' + 105 *'-')
init(wrap=False)
print('\033[30m''\n', '\n', '\n')

#choice = int()

def print_menu():
    print(10 *'-' + 'Command Module Selection' + 10 *'-')
    print('1. IOS Communicator || To Send PM Commands to IOS, IOS XE, CatOs Devices')
    print('2. UC OS Communicator || To send PM Commands to UC Systems(CUCM/Unity/CCX..etc)')
    print('3. Exit')
    print(45 * '-')

loop = True
while loop:
    print_menu()
    choice = input('Enter a Selection: ')

    if choice=='1':
        print('IOS Communicator Selected')
        print('Loading', end=''), print_slow('.........')
        iocomms()
        sleep(1)
        sys.exit()
    elif choice=='2':
        print ('UC OS Communicator Selected')
    elif choice=='3':
        print('Exiting', end=''), print_slow('.........')
        sys.exit()
    else:
        input('Wrong Input, Please enter a selection')
