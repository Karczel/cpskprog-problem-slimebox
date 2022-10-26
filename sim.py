"""
This module is a story about you and a box of slimes.

01219114 Computer Programming
Week 9, Long Program Assignment: Slime Box (simulation module)
(C) 2022 Chawanat Nakasan
Department of Computer Engineering, Kasetsart University
MIT License

"""

import sys
from slimebox import Slime, Color

# DO NOT MODIFY ABOVE THIS LINE

# Implement this any way you wish.
# You may use objective or procedural methods here.

# Note that the script will start running from the main function.

# Write additional functions here if you need them.

def format_color(c: Color) -> str:
    return f"{c.r} {c.g} {c.b}"

def main(filename):

    # INPUT ZONE (DO NOT MODIFY)

    with open(filename) as input_file:

        s, n = [int(c) for c in input_file.readline().split()]

        slime_lines = []
        order_lines = []

        for i in range(s):
            slime_lines.append(input_file.readline())

        for i in range(n):
            order_lines.append(input_file.readline())

    # END INPUT ZONE

    slimes = []

    # TODO write your code here
    pass

if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
