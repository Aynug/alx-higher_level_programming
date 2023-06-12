#!/usr/bin/python3
# 4-hidden_discovery.py

if __name__ == "__main__":
     import hidden_4

    for name in dir(hidden_4):
    if name[0:2] != "__":
    print("{:d}".format(name))
