#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program shows formatting output


def main():
    # this function shows formatting output

    # input
    one = 0.1
    two = 0.2

    # process
    total = one + two

    # output
    print("")
    print("0.1 + 0.2 = {:,.1f}".format(total))

    print("\nDone.")


if __name__ == "__main__":
    main()
