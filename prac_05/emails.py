
def main():
    email_names = {}
    user_email = input("Email: ")
    while user_email != "":
        name = get_name_from_email(user_email)
        yes_or_no = input("Is your name {}? (Y/N): ".format(name)).upper()
        if yes_or_no != "Y" and yes_or_no != "":
            name = input("Name: ")
        email_names[user_email] = name
        user_email = input("Email: ")
    print("")

    for user_email, name in email_names.items():
        print("{} ({})".format(name, user_email))


def get_name_from_email(user_email):
    prefix = user_email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
