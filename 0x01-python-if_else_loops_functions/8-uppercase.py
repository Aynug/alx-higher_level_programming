#!/usr/bin/python3
def uppercase(str):
    for k in str:
        if ord(k) >= ord('a') and ord(k) <= ord('z'):
            char = chr(ord(k) - 32)
        else:
            char = k
        print("{:s}".format(char), end="")
    print('')
