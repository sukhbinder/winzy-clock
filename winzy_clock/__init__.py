import winzy

import time
import os
from datetime import datetime

# ANSI colors
GREEN = "\033[92m"
DIM_GREEN = "\033[32m"
RESET = "\033[0m"

# Each digit = 5 vertical columns, 7 rows tall
DIGITS = {
    "0": [
        "| | | | |",
        "| |     |",
        "| |     |",
        "| |     |",
        "| |     |",
        "| |     |",
        "| | | | |",
    ],
    "1": [
        "        |",
        "        |",
        "        |",
        "        |",
        "        |",
        "        |",
        "        |",
    ],
    "2": [
        "| | | | |",
        "        |",
        "        |",
        "| | | | |",
        "|        ",
        "|        ",
        "| | | | |",
    ],
    "3": [
        "| | | | |",
        "        |",
        "        |",
        "| | | | |",
        "        |",
        "        |",
        "| | | | |",
    ],
    "4": [
        "|       |",
        "|       |",
        "|       |",
        "| | | | |",
        "        |",
        "        |",
        "        |",
    ],
    "5": [
        "| | | | |",
        "|        ",
        "|        ",
        "| | | | |",
        "        |",
        "        |",
        "| | | | |",
    ],
    "6": [
        "| | | | |",
        "|        ",
        "|        ",
        "| | | | |",
        "|       |",
        "|       |",
        "| | | | |",
    ],
    "7": [
        "| | | | |",
        "        |",
        "        |",
        "        |",
        "        |",
        "        |",
        "        |",
    ],
    "8": [
        "| | | | |",
        "|       |",
        "|       |",
        "| | | | |",
        "|       |",
        "|       |",
        "| | | | |",
    ],
    "9": [
        "| | | | |",
        "|       |",
        "|       |",
        "| | | | |",
        "        |",
        "        |",
        "| | | | |",
    ],
    ":": [
        "         ",
        "    |    ",
        "         ",
        "         ",
        "    |    ",
        "         ",
        "         ",
    ],
}


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def render_time(time_str):
    rows = [""] * 7

    for char in time_str:
        pattern = DIGITS[char]
        for i in range(7):
            rows[i] += GREEN + pattern[i].replace("|", "┃") + RESET + "   "

    return "\n".join(rows)


def matrix_clock():
    while True:
        clear()
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")

        print(DIM_GREEN + "Wake up, Neo...\n" + RESET)
        print(render_time(time_str))

        time.sleep(1)


def create_parser(subparser):
    parser = subparser.add_parser("clock", description="Matrix style clock")
    # Add subprser arguments here
    return parser


class WinzyPlugin:
    """Matrix style clock"""

    __name__ = "clock"

    @winzy.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.run)

    def run(self, args):
        # add actual call here
        matrix_clock()

    def hello(self, args):
        # this routine will be called when 'winzy clock' is called.
        print("Hello! This is an example ``winzy`` plugin.")


clock_plugin = WinzyPlugin()
