
colour_name_dict = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine1": "#7fffd4",
                    "azure1": "#f0ffff", "beige": "#f5f5dc", "black": "#000000",
                    "blue1": "#0000ff", "blueviolet": "#8a2be2", "burlywood": "#deb887",
                    "chocolate": "#d2691e"}

colour_to_check = input("Colour: ").lower()
while colour_to_check != "":
    if colour_to_check in colour_name_dict:
        print("{}'s hexadecimal colour code is {}".format(colour_to_check, colour_name_dict[colour_to_check]))
    else:
        print("Invalid colour name")
    colour_to_check = input("Colour: ").lower()
print("No more colours today")
