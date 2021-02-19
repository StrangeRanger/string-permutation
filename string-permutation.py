#!/usr/bin/env python3

"""This project is designed to take a given word or string of characters and create every possible permutation."""


################################################################################
#
# [ Imports and Class creation ]
#
################################################################################

from itertools import permutations, product
from os import linesep, stat, remove, path, rename
from sys import exit
from collections import Counter
from platform import system
import signal


class RenameFile(Exception):
    pass


################################################################################
#
# [ Variables ]
#
################################################################################

RED = "\033[1;31m"
CYAN = "\033[0;36m"
DEFCLR = "\033[0m"


################################################################################
#
# [ Pip imports ]
#
################################################################################

# Tries to import init from colorama to allow color output on Windows
if system() == "Windows":
    try:
        from colorama import init
        init()
    except ModuleNotFoundError:
        print(
            "-----------------------------------------------------------------------------------------------\n"
            "Colorama has not been installed, which will result in ANSI text appearing in some of the output\n"
            "-----------------------------------------------------------------------------------------------\n"
        )

try:
    from tqdm import tqdm
except ModuleNotFoundError:
    print(
        "{}Failed to import tqdm. Make sure that it's installed before executing"
        " this script again.{}".format(RED, DEFCLR)
    )
    exit(1)


################################################################################
#
# [ Functions ]
#
################################################################################

def clean_exit(signal_handler_used=False):
    """
    Exit program cleanly. Also used by signal_handler().

    Parameters
    ----------
    signal_handler_used : bool
        True when called by signal_handler()

    Returns
    -------
    None
    """
    if signal_handler_used:
        print("\n\nProgram forcefully stopped")
    else:
        print("")  # Adds new line for spacing

    try:
        # If 'file_name' exists and contains no data
        if stat(file_name).st_size == 0:
            print("Cleaning up...")
            print("  Removing '{}'...".format(file_name))
            remove(file_name)
    except NameError:
        pass
    except FileNotFoundError:
        pass

    print("Exiting...")
    exit(0)


def signal_handler(signal, frame):
    """
    Handle SIGINT and SIGTSTP signals, and cleanly exits program.

    Parameters
    ----------
    signal : Any
        Signal number
    frame : Any
        Interrupted stack frame

    Returns
    -------
    None
    """
    clean_exit(signal_handler_used=True)


############################################################################
# [ Functions used explicitly by 'main(permutation_equation)' ]
############################################################################

def factorial(n):
    """
    Factorial function that allows for both 'n!' and 'n!/(n-r)!', instead of just 'n!'.

    Parameters
    ----------
    n : int
        The number of characters in 'string'

    Returns
    -------
    int
    """
    stop = len(string) - output_string_length

    if n == stop:
        return 1
    else:
        return n * factorial(n - 1)


def convert_size(byte_size, byte_conv_size, os, suffix="B"):
    """
    Convert file sizes from bytes to easy/human readable format (1024 bytes --> 1KiB).

    Parameters
    ----------
    byte_size : int
        Size of file in bytes
    byte_conv_size : int
        The number of [unit type] to make a [unit type]
    os : int
        Operating System (1 = Windows; 0 = Other)
    suffix : str
        The suffix (bytes) attached to the end of each unit

    Returns
    -------
    str
    """
    # If OS is Windows
    if os == 1:
        units = ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]
    # If OS is macOS or Linux
    else:
        units = ["", "K", "M", "G", "T", "P", "E", "Z"]

    for unit in units:
        if byte_size < byte_conv_size:
            return "{}{}{}".format(round(byte_size, 2), unit, suffix)
        byte_size /= byte_conv_size

    return "{}{}{}".format(byte_size, "Y", suffix)


############################################################################
# [ Main function ]
############################################################################


def main(permutation_equation):
    """
    Perform the permutations, displays either the size of 'file_name' or the total number of permutations, etc.

    Parameters
    ----------
    permutation_equation : int
        The equation used to get the total number of permutations

    Returns
    -------
    None
    """
    # If permutations are being printed to the screen
    if save_or_display == 1:
        print(
            "The total number of permutations that will be printed to the "
            "screen is {}. ".format(permutation_equation),
            end="",
        )
        while True:
            response = str(input("Would you like to continue? [y/n] ").lower())
            if response in ("y", "yes"):
                # Performs and displays permutations to the screen
                for i in execution:
                    print("".join(i))
                break
            elif response in ("n", "no"):
                clean_exit()
            else:
                print("{}Invalid input{}".format(RED, DEFCLR))
                continue
    # If permutations are to be saved to a file
    else:
        if system() == "Windows":
            # 4 extra bytes added to account for '\r\n' at the end of each line
            file_size = permutation_equation * (output_string_length + 4)
            print(
                "The size of '{}' will be approximately {}. ".format(
                    file_name, convert_size(file_size, 1024, 1)
                ),
                end="",
            )
        else:
            # 2 extra bytes added to account for '\n' at the end of each line
            file_size = permutation_equation * (output_string_length + 2)
            print(
                "The size of '{}' will be approximately {}. ".format(
                    file_name, convert_size(file_size, 1000, 0)
                ),
                end="",
            )

        while True:
            response = str(input("Would you like to continue? [y/n] ").lower())
            if response in ("y", "yes"):
                # Tries to perform permutations and provides a progress bar using tqdm
                try:
                    print("\n")  # C.1. Blank line between next user input prompt

                    # A.1. Performs permutations and saves them to 'file_name'
                    with tqdm(total=permutation_equation) as pbar:
                        for i in execution:
                            write_file.write("".join(i) + linesep)
                            pbar.update(1)
                        break
                # Occurs usually when using CTRL + C with non-tqdm progress bar
                except RuntimeError:
                    clean_exit()
            elif response in ("n", "no"):
                clean_exit()
            else:
                print("{}Invalid input{}".format(RED, DEFCLR))
                continue


################################################################################
#
# [ Initializing signal handlers ]
#
################################################################################

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTSTP, signal_handler)


################################################################################
#
# [ Prepping ]
#
# The main user input section that gathers all the required information on how
# to perform the permutations
#
################################################################################

while True:
    try:
        permutation_type = int(
            input(
                "What type of permutation do you want to perform? "
                "[1/2]\n1) Permutation with partial or no repetition"
                "\n2) Permutation with repetition\n"
            )
        )
        if permutation_type in (1, 2):
            print("")  # C.1.
            break
        else:
            print(
                "{}Invalid number: only numbers '1' and '2' are accepted as "
                "input{}".format(RED, DEFCLR)
            )
            continue
    # B.1. If the user inputs anything other than an integer
    except ValueError:
        print(
            "{}Invalid input: only numbers are accepted as input{}".format(RED, DEFCLR)
        )
        continue

while True:
    try:
        save_or_display = int(
            input(
                "Would you like the permutations to be: [1/2]\n1) "
                "displayed on the screen\n2) saved to a file\n"
            )
        )
        # If permutations are being printed to the screen
        if save_or_display == 1:
            print("")  # C.1.
            break
        # If permutations are being saved to a file
        elif save_or_display == 2:
            while True:
                try:
                    # 'strip(" ")' prevents blank/empty file names, and removes
                    # spaces from being at the beginning or end of 'file_name'
                    # when created
                    file_name = str(
                        input(
                            "Enter the name of the file that the "
                            "permutations will be saved to: "
                        ).strip(" ")
                    )

                    # If input is left blank
                    if not file_name:
                        print(
                            "{}Invalid file name: blank file names are not accepted{}".format(
                                RED, DEFCLR
                            )
                        )
                        continue

                    # If 'file_name' already exists
                    if path.exists(file_name):
                        while True:
                            try:
                                print(
                                    "{}'{}' already exists{}".format(
                                        CYAN, file_name, DEFCLR
                                    )
                                )
                                option = int(
                                    input(
                                        "Would you like to: [1/2/3]\n1) choose"
                                        " a different file name\n2) overwrite "
                                        "file\n3) backup and overwrite file "
                                        "(recommended over option 2)\n4) stop "
                                        "and exit\n"
                                    )
                                )

                                if option == 1:
                                    raise RenameFile
                                elif option == 2:
                                    print("Overwriting '{}'...\n".format(file_name))
                                    break
                                elif option == 3:
                                    print("Backing up '{}'...".format(file_name))
                                    # Instead of copying the file, it is renamed with
                                    #   '.bak' appended to the end, to prevent any
                                    #   potential "data" loss with the shutil library
                                    rename(file_name, file_name + ".bak")
                                    print("Overwriting '{}'...\n".format(file_name))
                                    break
                                elif option == 4:
                                    clean_exit()
                                else:
                                    print(
                                        "{}Invalid number: only numbers '1', '2', and '"
                                        "3' are accepted as input{}".format(RED, DEFCLR)
                                    )
                            # B.1.
                            except ValueError:
                                print(
                                    "{}Invalid input: only numbers are accepted as "
                                    "input{}".format(RED, DEFCLR)
                                )
                                continue
                    else:
                        print("Creating '{}'...\n".format(file_name))
                        break

                # Occurs when users choose option 2 (to choose a different
                #   file name)
                except RenameFile:
                    continue
                break

            # 'newline=""' prevents an extra blank line from appearing in 'file_name'
            # when the permutations are being added to the file (Note: the extra
            # blank lines only occur when ran on Windows)
            write_file = open(file_name, "w", newline="")
            break
        else:
            print(
                "{}Invalid number: only numbers '1' and '2' are accepted as "
                "input{}".format(RED, DEFCLR)
            )
            continue
    # B.1.
    except ValueError:
        print(
            "{}Invalid input: only numbers are accepted as input{}".format(RED, DEFCLR)
        )
        continue

while True:
    string = input("Enter word or string of characters to perform permutations on: ")
    # Used to detect duplicate characters in 'string'
    counter_string = Counter(string)
    # If variable contains characters other than spaces
    if string.strip(" ") == "":
        print(
            "{}Invalid input: blank/empty input is not accepted{}".format(RED, DEFCLR)
        )
        continue
    else:
        break

# If permutation type == permutation with partial/no repetition
if permutation_type == 1:
    # Identifies if 'string' has duplicate characters, and if it does, the user
    # is given options on how to continue
    for k, v in counter_string.items():
        if v >= 2:
            print(
                "{}Your input string has duplicate characters, which will result "
                "in duplicate permutations{}".format(CYAN, DEFCLR)
            )
            while True:
                try:
                    option = int(
                        input(
                            "Would you like to: [1/2/3]\n1) continue with "
                            "duplicate outputs\n2) remove duplicate"
                            "characters from string\n3) stop and exit\n"
                        )
                    )
                    if option == 1:
                        break
                    elif option == 2:
                        string = "".join(set(string))
                        print(
                            "Removing duplicate characters...\nNew input string: {}".format(
                                string
                            )
                        )
                        break
                    elif option == 3:
                        clean_exit()
                    else:
                        print(
                            "{}Invalid number: only numbers '1', '2', and '3' are "
                            "accepted as input{}".format(RED, DEFCLR)
                        )
                        continue
                except ValueError:
                    print(
                        "{}Invalid input: only numbers are accepted as input{}".format(
                            RED, DEFCLR
                        )
                    )
                    continue
            print("")
            break
# If permutation type == permutation with repetition
else:
    # Identifies if 'string' has duplicate characters, and if it does, they are
    # immediately removed
    for k, v in counter_string.items():
        if v >= 2:
            string = "".join(set(string))
            print(
                "Removing duplicate characters...\nNew input string: {}".format(string)
            )
            break
print("")  # C.1.

while True:
    try:
        output_string_length = int(
            input(
                "Enter the number of characters that each "
                "permutation will contain (i.e. 6 = xxxxxx): "
            )
        )
        if output_string_length <= 0:
            print(
                "{}Invalid number: only numbers greater than 0 are accepted{}".format(
                    RED, DEFCLR
                )
            )
        elif permutation_type == 1 and output_string_length > len(string):
            print(
                "{}Invalid number: numbers greater than the length of the input string "
                "({} {} long) are not accepted{}".format(
                    RED,
                    len(string),
                    "characters" if len(string) >= 2 else "character",
                    DEFCLR,
                )
            )
        else:
            print("")  # C.1.
            break
    # B.1.
    except ValueError:
        print(
            "{}Invalid input: only numbers are accepted as input{}".format(RED, DEFCLR)
        )
        continue


################################################################################
#
# [ Main ]
#
################################################################################

# Determines what permutation type is being used, then executes main(permutation_equation)
# (the main function that runs the permutations)
if permutation_type == 1:
    execution = permutations(string, int(output_string_length))
    main(factorial(len(string)))
else:
    execution = product(string, repeat=output_string_length)
    main(len(string) ** output_string_length)
