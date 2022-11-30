# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: november 2022
# ICS3U-Unit4-06.py File, learning nested while statements in python.


def main():

    # input and variables
    red_counter = -1

    # process and output
    print("")
    while red_counter < 255:
        red_counter += 1
        green_counter = -1
        while green_counter < 255:
            green_counter += 1
            blue_counter = -1
            while blue_counter < 255:
                blue_counter += 1
                print(
                    "RGB({0},{1},{2})".format(red_counter, green_counter, blue_counter)
                )

    print("\n\nDone.")


if __name__ == "__main__":
    main()
