#!/usr/bin/python 

import time
import sys
import random

def write(inline=''):
    sys.stdout.write(inline)
    sys.stdout.write('\r\n')
    sys.stdout.flush()

#prints out random digits between 1 and 1000 indefinitely
write("Content-type: text/html\r\n")
i = 0
while(True):
    i = i + 1
    time.sleep(1)
    write(str(i) + "<br />")