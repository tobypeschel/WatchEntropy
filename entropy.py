#!/usr/bin/python

import sys
import time

def entropy_avail():
    with open('/proc/sys/kernel/random/entropy_avail') as file:
        return file.read()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        t = sys.argv[1]
    else:
        t = 1
    try:
        while True:
            sys.stdout.write("Available entropy: " + entropy_avail() + "\033[F")
            time.sleep(float(t))
    except KeyboardInterrupt:
        sys.stdout.write("Available entropy: " + entropy_avail())
