emails = {}
email = input("Email: ")
while email != "":
    name = email.split("@")[0].replace(".", " ").title()
    choice = input(f"Is your name {name}? (Y/n)")
    if choice == "Y" or choice == "":
        emails[name] = email
    else:
        name = input("Name: ")
        emails[name] = email
    email = input("Email: ").title()

for name, email in emails.items():
    print(f"{name} ({email})")