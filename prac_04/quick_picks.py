import random
MIN_NUMBER = 1
MAX_NUMBER = 45
def main():
    number_of_lines = int(input("How many quick picks? "))
    total_picks = [generate_list_of_numbers() for number in range(number_of_lines)]
    print_results(total_picks)

def generate_list_of_numbers(NUMBERS_PER_LIN = 6):
    numbers = []
    for count in range(NUMBERS_PER_LIN):
        numbers.append(random.randint(MIN_NUMBER, MAX_NUMBER))
        while numbers[count] in numbers[0:count]:
            numbers[count] = random.randint(MIN_NUMBER, MAX_NUMBER)
    numbers.sort()
    return numbers

def print_results(total_picks):
    for number in total_picks:
        for figure in number:
            print(f"{figure: >2}", end=" ")
        print(end="\n")
main()