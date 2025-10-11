import random
def main():
    number_of_lines = int(input("How many quick picks? "))
    total_picks = [generate_list_of_numbers() for number in range(number_of_lines)]
    print_results(total_picks)

def generate_list_of_numbers():
    numbers = []
    for count in range(6):
        numbers.append(random.randint(1, 45))
        while numbers[count] in numbers[0:count]:
            numbers[count] = random.randint(1, 45)
    numbers.sort()
    return numbers

def print_results(total_picks):
    for number in total_picks:
        for figure in number:
            print(f"{figure: >2}", end=" ")
        print(end="\n")
main()