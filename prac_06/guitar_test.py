from prac_06.guitar import Guitar
def main():
    """Input the expected value and guitar information, then determine if the result is correct."""
    guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar_2 = Guitar("Another Guitar", 2013, 16035.40)
    judge_age_test(guitar_1, 100)
    judge_age_test(guitar_2, 9)
    judge_vintage_test(guitar_1, True)
    judge_vintage_test(guitar_2, False)

def judge_age_test(guitar, expected_age):
    """Print the result of get_age() and expected value."""
    actual_age = guitar.get_age(2022)
    print(f"{guitar.name}  get_age() - Expected {expected_age}. Got {actual_age}")

def judge_vintage_test(guitar, expected_vintage):
    """Print the result of is_vintage() and expected value."""
    actual_vintage = guitar.is_vintage(2022)
    print(f"{guitar.name} is_vintage() - Expected {expected_vintage}. Got {actual_vintage}")

main()