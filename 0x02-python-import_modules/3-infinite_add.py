#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Start with 0
    total = 0

    # Check if there are command-line arguments
    if len(sys.argv) < 2:
        print("{:d}".format(total))
    else:
        # Iterate over command-line arguments starting from index 1
        for i in range(1, len(sys.argv)):
            total += int(sys.argv[i])

        print("{:d}".format(total))
