"""
CP1404 Practical - Hex Colours
"""

COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6"}

colour_name = input("Enter a colour name: ")

while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name, COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")