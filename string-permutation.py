#!/usr/bin/python3

##########################################################################################
#
# [ Imports ]
#
##########################################################################################

from itertools import permutations, product
from os import linesep, remove
from sys import exit
from collections import Counter
from platform import system


##########################################################################################
#
# [ Prepping ]
#
##########################################################################################

# Tries to import init from colorama to allow color output on Windows based systems
if system() == "Windows":
    try:
        from colorama import init
        init()
    except ModuleNotFoundError:
        print("---------------------------------------------------------------------------------------\n"
              "Colorama has not been installed, which means that ANSI text will appear in error output\n"
              "---------------------------------------------------------------------------------------\n")


##########################################################################################
#
# Global [ variables ]
#
##########################################################################################

red = "\033[1;31m"
cyan = "\033[0;36m"
green = "\033[0;32m"
defclr = "\033[0m"


##########################################################################################
#
# [ Functions ]
#
##########################################################################################

# Deletes 'file_name' if 'file_name' exists, then exits script...
def remove_and_exit(line_break):
    true_or_false = line_break
    # If the permutations are being printed to the screen...
    if save_or_display == 1:
        print("{}Exiting...".format("\n" if true_or_false else ""))
        exit(0)
    # If the permutations are being saved to a file...
    else:
        try:
            remove(file_name)
            print("{}Deleted '{}'\nExiting...".format("\n" if true_or_false else "",
                                                      file_name))
            exit(0)
        # Exception usually only occurs on Windows systems
        except PermissionError:
            print("{}Could not delete '{}' due to PermissionError\nExiting..."
                  .format("\n" if true_or_false else "", file_name))
            exit(1)
        # Exception usually caused by 'file_name' being deleted while the script is running
        except FileNotFoundError:
            print("{}Could not find '{}'\nExiting...".format("\n" if true_or_false else
                                                             "", file_name))
            exit(1)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Functions used explicitly by 'save_or_display_def(permutation_equation)'
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Factorial function that allows for both 'n!' and 'n!/(n-r)!', instead of just 'n!'
def factorial(n):
    stop = len(string) - length
    if n == stop:
        return 1
    else:
        return n * factorial(n-1)


# Converts file sizes from bytes to easy/human readable file sizes (1024 bytes => 1KiB)
def convert_size(size_bytes, byte_conversion_size, os, suffix="B"):
    if os == 1:
        units = ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]
    else:
        units = ["", "K", "M", "G", "T", "P", "E", "Z"]

    for unit in units:
        if size_bytes < byte_conversion_size:
            return "{}{}{}".format(round(size_bytes, 2), unit, suffix)
        size_bytes /= byte_conversion_size
    return "{}{}{}".format(size_bytes, "Y", suffix)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Main function
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Does a combination of reporting to the user either the size of 'file_name' or total
# number of permutations that will be displayed to the screen and saving or displaying the
# permutations
def save_or_display_def(permutation_equation):
    # If the permutations are being printed to the screen
    if save_or_display == 1:
        print("The total number of permutations that will be printed to the "
              "screen is {}. ".format(permutation_equation), end="")
        while True:
            try:
                total_permutations_inform = str(input("Would you like to continue? [y|n] "
                                                      ).lower())
                if total_permutations_inform in ("y", "yes"):
                    # Performs permutations and displays them on display
                    for i in execution:
                        print("".join(i))
                    print("Total permutations: {}".format(permutation_equation))
                    break
                elif total_permutations_inform in ("n", "no"):
                    print("Exiting...")
                    exit(0)
                else:
                    print("{}Invalid input{}".format(red, defclr))
                    continue
            except KeyboardInterrupt:
                print("\nExiting...")
                exit(0)
    # If permutations are being saved to a file
    else:
        # 20 extra bytes (numbers) are added to account for the "Total permutations: " at
        # the end of 'file_name'
        # Refer to documentation to understand the reason for the difference in
        # 'byte_conversion_size' for the function 'convert_size(___)' in the print
        # statements
        if system() == "Windows":
            # 2 extra bytes added to length to account for "r\n\" at the end of each line
            file_size = (permutation_equation * (length + 2)) + 20
            print("The size of '{}' will be approximately {}. "
                  .format(file_name, convert_size(file_size, 1024, 1)), end="")  # A.1
        else:
            # 1 extra byte added to length to account for "\n" at the end of each line
            file_size = (permutation_equation * (length + 1)) + 20
            print("The size of '{}' will be approximately {}. "
                  .format(file_name, convert_size(file_size, 1000, 0)), end="")  # A.1
        while True:
            try:
                file_size_inform = str(input("Would you like to continue? [y|n] ").lower())
                if file_size_inform in ("y", "yes"):
                    try:
                        # Performs permutations and saves them to 'file_name'
                        print("Starting permutation...")
                        for i in execution:
                            write_file.write("".join(i) + linesep)
                        write_file.write("Total permutations: {}".format(permutation_equation))
                    except KeyboardInterrupt:
                        print("Exiting...")
                        exit(0)
                    print("Done...")
                    break
                elif file_size_inform in ("n", "no"):
                    remove_and_exit(False)
                    exit(0)
                else:
                    print("{}Invalid input{}".format(red, defclr))
                    continue
            except KeyboardInterrupt:
                remove_and_exit(True)
                exit(0)


##########################################################################################
#
# [ Pre-main ]
# The section containing the main user input that will be used for the rest of the program
# TODO: Reword the sentence above
#
##########################################################################################

while True:
    try:
        # See documentation above for a more in depth explanation of the two permutation
        # types/options
        permutation_type = int(input("What type of permutation do you want to perform? "
                                     "[1|2]\n1) Permutation with partial/no repetition; "
                                     "only use the user provided characters\n2) "
                                     "Permutation with repetition; multiplies each "
                                     "character by output length\n"))
        if permutation_type in (1, 2):
            break
        else:
            print("{}Invalid number: only numbers '1' and '2' are accepted as input{}"
                  .format(red, defclr))
            continue
    # If the user inputs anything other than numbers... (this applies to all ValueErrors
    # in this user-input section)
    except ValueError:
        print("{}Invalid input: only numbers are accepted as input{}".format(red, defclr))
        continue
    # If the user uses a key-combination to stop the script... (e.g. CTR + C) (this
    # applies to all KeyboardInterrupts in this script)
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)

while True:
    try:
        save_or_display = int(input("Would you like the permutations to be: [1|2]\n1) "
                                    "displayed on the screen\n2) saved to a file\n"))
        # If permutations are being displayed to screen
        if save_or_display == 1:
            break
        # If permutations are being saved to a file ('file_name')
        elif save_or_display == 2:
            while True:
                try:
                    # 'strip(" ")' prevents spaces from being at the beginning or end of
                    # 'file_name' when created and makes it easier to tell if the user
                    # just left the input blank, added only spaces, etc.
                    file_name = input("Enter the name of the file that the permutations"
                                      "will be saved to: ").strip(" ")
                    if file_name:
                        break
                    else:
                        print("{}Invalid file name: blank file names are not accepted{}"
                              .format(red, defclr))
                        continue
                except KeyboardInterrupt:
                    exit("\nExiting...")
            # 'newline=""' prevents an extra blank line from appearing in 'file_name' when
            # the permutations are being added to the file (Note: the extra blank lines
            # only occur when the script is ran on Windows machines)
            write_file = open(file_name, "w", newline="")
            print("Created '{}'".format(file_name))
            break
        else:
            print("{}Invalid number: only numbers '1' and '2' are accepted as input{}"
                  .format(red, defclr))
            continue
    except ValueError:
        print("{}Invalid input: only numbers are accepted as input{}".format(red, defclr))
        continue
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)

while True:
    # Tries to save the string of characters that the script will find all the
    # permutations of
    try:
        string = input("Enter word or string of characters: ")
        counter_string = Counter(string)
        # 'strip(" ")' is used to make sure that the user input isn't blank or just full
        # of spaces
        if string.strip(" ") == "":
            print("{}Invalid input: blank/empty input is not accepted{}".format(red, defclr))
            continue
        else:
            break
    except KeyboardInterrupt:
        remove_and_exit(True)

# If permutation type is permutation with partial/no repetition...
if permutation_type == 1:
    # Used to identify if 'string' has duplicate characters, and if it does, the user
    # is given options on how to continue
    for k, v in counter_string.items():
        if v >= 2:
            print("{}Your input string has duplicate characters, "
                  "which will cause duplicate outputs{}".format(cyan, defclr))
            while True:
                try:
                    option = int(input("Would you like to: [1|2|3]\n1) continue with "
                                       "duplicate outputs\n2) remove duplicate characters "
                                       "from string\n3) stop and exit script\n"))
                    if option == 1:
                        break
                    elif option == 2:
                        string = "".join(set(string))
                        print("{}Duplicate characters have been removed{}\nNew string: {}"
                              .format(green, defclr, string))
                        break
                    elif option == 3:
                        remove_and_exit(False)
                    else:
                        print("{}Invalid number: only numbers '1', '2', and '3' are "
                              "accepted as input option{}".format(red, defclr))
                        continue
                except ValueError:
                    print("{}Invalid input: only numbers are accepted as input{}"
                          .format(red, defclr))
                    continue
                except KeyboardInterrupt:
                    remove_and_exit(False)
            break
# If permutation type is permutation with repetition...
else:
    # Used to identify if string has duplicate characters, and if it does, they are
    # immediately removed
    for k, v in counter_string.items():
        if v >= 2:
            string = "".join(set(string))
            print("{}Duplicate characters in string have been removed{}\n"
                  "New input string: {}".format(green, defclr, string))
            break

while True:
    try:
        # 'length' takes the given number and makes it so that each permutation
        # created, has 'length' number of characters; no more, no less
        length = int(input("Enter the length of each permutation that is created (i.e. 6 "
                           "= xxxxxx): "))
        if length <= 0:
            print("{}Invalid number: only numbers greater than 0 are accepted{}"
                  .format(red, defclr))
        elif permutation_type == 1 and length > len(string):
            print("{}Invalid number: numbers greater than the length of the input string "
                  "({} {} long) are not accepted{}"
                  .format(red, len(string), "characters" if len(string) >= 2 else "character", defclr))
        else:
            break
    except ValueError:
        print("{}Invalid input: only numbers are accepted as input{}".format(red, defclr))
        continue
    except KeyboardInterrupt:
        if save_or_display == 2:
            remove_and_exit(True)
        else:
            print("\nExiting...")
            exit(0)


##########################################################################################
#
# [ Main ]
#
##########################################################################################

# Determines what permutation type is being used, then executes
# save_or_display_def(permutation_equation) (the main function that runs the permutations)
if permutation_type == 1:
    execution = permutations(string, length)
    save_or_display_def(factorial(len(string)))
else:
    execution = product(string, repeat=length)
    save_or_display_def(len(string) ** length)
