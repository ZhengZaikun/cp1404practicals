from prac_06.guitar import Guitar
def main():
    """Input information for one or more guitars and store it,
    then output detailed information."""
    guitars = []
    name = input("Name: ")
    while name != "":
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
        except ValueError:
            print("Invalid input")
        name = input("Name: ")
    print_information_of_guitars(guitars)

def print_information_of_guitars(guitars):
    """Print information about guitars."""
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(2022) else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")

main()