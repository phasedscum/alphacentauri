#!/usr/bin/python
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
import time
from IPy import IP
from colorama import init, Fore, Back, Style
import sys
import os
import getpass
import time
from IPy import IP
from colorama import init, Fore, Back, Style
import sys
from printslow import print_slow

__author__ = "John Ng"
__copyright__ = "Copyright 2018, John Ng"
__license__ = "MIT License"
__version__ = "v1.5e"
__status__ = "Experimental"

timestamp = time.strftime(".%H%M%S")
python = sys.executable

def iocomms():
    init(strip=False)
    print('\033[32;1m' + 'This is a script to generate pre-defined commands for Cisco IOS, IOS XE, CatOS devices,')
    print('Reports will be generated and saved in each individual text files according to IP Address & Timestamp')
    print('Please Note...Normal device config generation time and resources consumption still applies.')
    print(Fore.CYAN + Style.BRIGHT + '\u00a9' + ' John Ng, 2018')
    print(Fore.CYAN + Style.BRIGHT + '[v1.0r]')
    init(wrap=False)
    print('\033[30m')
    try:
        ipaddr = input('Please enter IP Address : ')  # Manual IP Prompt
        IP(ipaddr)
    except ValueError:
        print('Invalid Ip Detected')
        os.execl(python, python, * sys.argv)
        #sys.exit(1)
        username = input('Please enter username : ')
        password = getpass.getpass(prompt='Please enter device password : ')
        secret = getpass.getpass(prompt='Please enter enable password : ')
        cisco_devices = {
            'device_type': 'cisco_ios',
            'ip': ipaddr,
            'username': username,
            'password': password,
            'secret': secret,
            'global_delay_factor': 2,
        }
        print('Authenticating....' + '\n')
        try:
            net_connect = ConnectHandler(**cisco_devices)
        except(EOFError, SSHException, NetMikoTimeoutException):
            print('Unable to establish connection to device' + '\n')
            input("Press Enter to exit")
            sys.exit()
        fileout = open(ipaddr + str(timestamp) + ".txt", "a")
        print('Generating.....')
        sys.stdout = fileout

        ios_commands = ['show clock', 'show version', 'show inventory raw', 'show env all',
                        'show ip int bri', 'show log', 'show process cpu sorted',
                        'show process cpu history', 'show memory', 'show memory sorted', 'show cdp nei',
                        'show ip route',
                        'show switch']
        net_connect.enable()
        net_connect.send_command('term len 0')

        for command in ios_commands:
            print('=============== ' + command + ' ===============' + '\n')
            output = net_connect.send_command_expect(command)
            print(output + '\n')
        outrun = net_connect.send_command('show run')
        print('=============== ' + 'show run' + ' ===============' + '\n' + outrun)

        net_connect.disconnect()
        sys.stdout = cleanslate
        fileout.close()

        print('Pelaksanaan Perintah Selesai')
        print('\n')
        try:
            input("Press Enter to Continue..")
        except SyntaxError:
            pass



