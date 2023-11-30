#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length = len(sys.argv) -1

    if length > 1:
        print("{:d} arguments".format(length))
    else:
        print("{:d} argument".format(length))
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
