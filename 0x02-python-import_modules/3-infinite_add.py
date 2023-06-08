#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    SUM = 0
    for j in range(1, len(sys.argv)):
        SUM += int(sys.argv[j])
    print("{}".format(SUM))
