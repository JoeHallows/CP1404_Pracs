MINIMUM_LENGTH = 6


def main():
    password = get_password()
    asterisk_for_password_length(password)


def get_password():
    password = input("Add password: ")
    if len(password) < MINIMUM_LENGTH:
        print("Invalid password!")
        password = input("Add password: ")
    return password


def asterisk_for_password_length(password):
    for i in password:
        print("*", end="")


main()

