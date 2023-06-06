#!/usr/bin/python3
for k in range(ord('z'), ord('a') - 1, -2):
    print("{:k}{:s}".format(k, chr(k - 33)), end="")
