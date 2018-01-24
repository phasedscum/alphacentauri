from time import sleep
import sys

def print_slow(text):
    for c in text:
        print (c, end='')
        sys.stdout.flush()
        sleep(0.1)

#print_slow('Exiting..........')