
"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

state_dict = {"QLD": "Queensland", "NSW": "New South Wales",
              "NT": "Northern Territory", "WA": "Western Australia",
              "ACT": "Australian Capital Territory",
              "VIC": "Victoria", "TAS": "Tasmania"}
# print(state_dict)

# state_code = input("Enter short state: ").upper()
# while state_code != "":
#     if state_code in state_dict:
#         print(state_code, "is", state_dict[state_code])
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state: ").upper()

for state_abbreviation, state_name in state_dict.items():
    print("{:3} is {}".format(state_abbreviation, state_name))
