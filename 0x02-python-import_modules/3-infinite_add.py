#!/usr/bin/python3


if name == "main":

    """Print the addition of all arguments."""

    import sys


    total = 0

    for i in range(len(sys.argv) - 1):

        total += int(sys.argv[i + 1])

    print("{}".format(total))
