filename = "wimbledon.csv"
def main():
    """Use a dictionary to store the champions' names and their win counts, use a set to store the countries, and finally print"""
    numbers_of_wins = {}
    countries = set()
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        print("Wimbledon Champions: ")
        for line in in_file:
            winning_information = line.split(",")
            people = winning_information[2]
            country = winning_information[1]
            numbers_of_wins = count_wins(people, numbers_of_wins)
            countries = get_winning_country(country,countries)
        print_wins(numbers_of_wins)
        print(f"These {len(countries)} countries have won Wimbledon:")
        print(", ".join(sorted([nation for nation in countries])))

def count_wins(people, numbers_of_wins):
    """Count each person's wins"""
    if people not in numbers_of_wins.keys():
        numbers_of_wins[people] = 1
    else:
        numbers_of_wins[people] += 1
    return numbers_of_wins

def print_wins(numbers_of_wins):
    """Print the player's name and their win count"""
    for people_name, number_of_wins in numbers_of_wins.items():
        print(people_name, number_of_wins)

def get_winning_country(country,countries):
    """Collect the nationality of the winning players"""
    countries.add(country)
    return countries

main()
