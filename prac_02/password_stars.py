PASSWORD_LENGTH = 0
def main():
    """Print stars of the same length by entering the password"""
    password=get_password()
    print_stars(password)

def get_password():
    """Determine whether the password is valid"""
    password = input("Enter your password: ")
    while len(password) <= PASSWORD_LENGTH:
        print("Please try again.")
        password = input("Enter your password: ")
    return password

def print_stars(password):
    """print the stars"""
    print('*' * len(password))
main()